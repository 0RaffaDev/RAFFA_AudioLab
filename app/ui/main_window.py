from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from app.ui.pages.songs_page import SongsPage

from app.ui.player_bar import PlayerBar
from app.ui.sidebar import Sidebar
from app.ui.styles import get_styles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Raffa AudioLab")
        self.resize(1200, 750)
        self.setMinimumSize(900, 600)

        self.setStyleSheet(get_styles())

        self.create_interface()

    def create_interface(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Zona principal
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        from PySide6.QtWidgets import QHBoxLayout

        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(0)

        # Menú lateral
        self.sidebar = Sidebar()
        self.sidebar.section_changed.connect(self.change_page)

        top_layout.addWidget(self.sidebar)

        # Páginas centrales
        self.pages = QStackedWidget()
        self.pages.setObjectName("pages")

        self.create_pages()

        top_layout.addWidget(self.pages, 1)

        # Reproductor inferior
        self.player_bar = PlayerBar()

        main_layout.addLayout(top_layout, 1)
        main_layout.addWidget(self.player_bar)


    def create_pages(self):

        sections = [
            ("Inicio", "Bienvenido a Raffa AudioLab"),
            ("Canciones", "Tu biblioteca musical"),
            ("Samples", "Tu colección de samples"),
            ("Audio Analyzer", "Analizador de audio"),
            ("Configuración", "Configuración de la aplicación"),
        ]

        self.page_indexes = {}

        for name, title in sections:

            if name == "Canciones":
                page = SongsPage()

            else:
                page = QWidget()
                layout = QVBoxLayout(page)

                layout.setContentsMargins(35, 35, 35, 35)

                heading = QLabel(title)
                heading.setObjectName("pageTitle")

                layout.addWidget(heading)
                layout.addStretch()

            self.page_indexes[name] = self.pages.count()
            self.pages.addWidget(page)

    def change_page(self, section):
        if section in self.page_indexes:
            index = self.page_indexes[section]
            self.pages.setCurrentIndex(index)