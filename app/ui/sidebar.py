from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Sidebar(QFrame):
    section_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(230)
        self.buttons = {}

        self.create_sidebar()

    def create_sidebar(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 25, 15, 20)
        layout.setSpacing(8)

        logo = QLabel("RAFFA AUDIOLAB")
        logo.setObjectName("logo")

        layout.addWidget(logo)
        layout.addSpacing(35)

        sections = [
            ("⌂", "Inicio"),
            ("♫", "Canciones"),
            ("▤", "Samples"),
            ("◉", "Audio Analyzer"),
        ]

        for icon, section in sections:
            button = QPushButton(f"{icon}     {section}")
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setCheckable(True)
            button.clicked.connect(
                lambda checked=False, name=section: self.select_section(name)
            )

            self.buttons[section] = button
            layout.addWidget(button)

        layout.addStretch()

        settings_button = QPushButton("⚙     Configuración")
        settings_button.setCursor(Qt.CursorShape.PointingHandCursor)
        settings_button.setCheckable(True)
        settings_button.clicked.connect(
            lambda: self.select_section("Configuración")
        )

        self.buttons["Configuración"] = settings_button
        layout.addWidget(settings_button)

        self.select_section("Inicio")

    def select_section(self, section):
        for name, button in self.buttons.items():
            button.setChecked(name == section)

        self.section_changed.emit(section)
