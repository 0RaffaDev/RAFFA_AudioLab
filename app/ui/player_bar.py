from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
)


class PlayerBar(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(95)

        self.playlist = []
        self.current_index = -1

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()

        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(0.7)

        self.create_player()

        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)
        self.player.mediaStatusChanged.connect(self.check_media_status)

    def create_player(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(25, 10, 25, 10)

        self.song_label = QLabel("Ninguna canción seleccionada")

        open_button = QPushButton("＋")
        previous_button = QPushButton("⏮")
        self.play_button = QPushButton("▶")
        next_button = QPushButton("⏭")

        self.position_label = QLabel("00:00")
        self.duration_label = QLabel("00:00")

        self.progress_slider = QSlider(Qt.Orientation.Horizontal)
        self.progress_slider.setRange(0, 0)
        self.progress_slider.sliderMoved.connect(self.change_position)

        open_button.clicked.connect(self.open_audio)
        previous_button.clicked.connect(self.previous_track)
        self.play_button.clicked.connect(self.toggle_playback)
        next_button.clicked.connect(self.next_track)

        for button in [
            open_button,
            previous_button,
            self.play_button,
            next_button,
        ]:
            button.setCursor(Qt.CursorShape.PointingHandCursor)

        layout.addWidget(self.song_label)
        layout.addWidget(open_button)
        layout.addWidget(previous_button)
        layout.addWidget(self.play_button)
        layout.addWidget(next_button)
        layout.addWidget(self.position_label)
        layout.addWidget(self.progress_slider, 1)
        layout.addWidget(self.duration_label)

    def open_audio(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Seleccionar archivos de audio",
            "",
            "Audio (*.mp3 *.wav *.ogg *.flac *.m4a)"
        )

        if files:
            self.playlist.extend(files)

            if self.current_index == -1:
                self.current_index = 0
                self.load_current_track()

    def load_current_track(self):
        if not self.playlist:
            return

        file_path = self.playlist[self.current_index]

        self.player.setSource(QUrl.fromLocalFile(file_path))

        filename = file_path.replace("\\", "/").split("/")[-1]
        self.song_label.setText(filename)

        self.player.play()
        self.play_button.setText("Ⅱ")

    def toggle_playback(self):
        if self.current_index == -1:
            self.open_audio()
            return

        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.play_button.setText("▶")
        else:
            self.player.play()
            self.play_button.setText("Ⅱ")

    def previous_track(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_current_track()

    def next_track(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.load_current_track()

    def change_position(self, position):
        self.player.setPosition(position)

    def update_position(self, position):
        self.progress_slider.setValue(position)
        self.position_label.setText(self.format_time(position))

    def update_duration(self, duration):
        self.progress_slider.setRange(0, duration)
        self.duration_label.setText(self.format_time(duration))

    def format_time(self, milliseconds):
        seconds = milliseconds // 1000
        minutes = seconds // 60
        seconds = seconds % 60

        return f"{minutes:02}:{seconds:02}"

    def check_media_status(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.next_track()