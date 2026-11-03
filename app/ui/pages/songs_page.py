
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QListWidget,
    QMessageBox,
)

from app.core.library_manager import LibraryManager
from PySide6.QtWidgets import QListWidgetItem

class SongsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.library = LibraryManager()

        self.create_interface()
        self.load_songs()

    def create_interface(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(35, 35, 35, 35)
        layout.setSpacing(20)

        heading = QLabel("Tu biblioteca musical")
        heading.setObjectName("pageTitle")

        description = QLabel(
            "Organizá y reproducí toda tu música desde AudioLab."
        )

        buttons_layout = QHBoxLayout()

        import_button = QPushButton("Importar canciones")
        folder_button = QPushButton("Importar carpeta")

        import_button.clicked.connect(self.import_files)
        folder_button.clicked.connect(self.import_folder)

        buttons_layout.addWidget(import_button)
        buttons_layout.addWidget(folder_button)
        buttons_layout.addStretch()

        self.song_list = QListWidget()
        self.song_list.itemDoubleClicked.connect(
            self.play_selected_song
        )

        layout.addWidget(heading)
        layout.addWidget(description)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.song_list)

    def load_songs(self):
        self.song_list.clear()

        self.songs = self.library.repository.get_all("song")

        for song in self.songs:
            self.song_list.addItem(f"{song.name}  •  {song.format}")
    def import_files(self):

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Seleccionar canciones",
            "",
            "Archivos de audio (*.mp3 *.wav *.flac *.ogg *.m4a *.aac *.wma)"
        )

        if not files:
            return

        imported = 0

        for file_path in files:
            success, message = self.library.importar_archivo(
                file_path,
                "song"
            )

            if success:
                imported += 1

        self.load_songs()

        QMessageBox.information(
            self,
            "Importación finalizada",
            f"Se importaron {imported} canciones."
        )

    def import_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar carpeta musical"
        )

        if not folder:
            return

        imported = self.library.importar_carpeta(
            folder,
            "song"
        )

        self.load_songs()

        QMessageBox.information(
            self,
            "Importación finalizada",
            f"Se importaron {imported} canciones."
        )
    def play_selected_song(self, item):
        index = self.song_list.row(item)

        if 0 <= index < len(self.songs):
            song = self.songs[index]

            playlist = [media.file_path for media in self.songs]

            self.window().player_bar.play_file(
                song.file_path,
                playlist
            )