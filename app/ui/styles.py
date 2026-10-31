def get_styles():
    return """
    QMainWindow {
        background-color: #111116;
    }

    QWidget {
        background-color: #111116;
        color: #E8E6EF;
        font-family: Segoe UI;
        font-size: 10pt;
    }

    #logo {
        color: #A879FF;
        font-size: 17px;
        font-weight: bold;
        letter-spacing: 2px;
    }

    Sidebar {
        background-color: #191820;
        border-right: 1px solid #292631;
    }

    QPushButton {
        background-color: transparent;
        color: #A7A4B3;
        border: none;
        border-radius: 8px;
        padding: 12px;
        text-align: left;
    }

    QPushButton:hover {
        background-color: #292432;
        color: #FFFFFF;
    }

    QPushButton:checked {
        background-color: #34234F;
        color: #C9A7FF;
        border-left: 3px solid #A879FF;
    }

    #pages {
        background-color: #111116;
    }

    #pageTitle {
        color: #FFFFFF;
        font-size: 25px;
        font-weight: bold;
    }

    PlayerBar {
        background-color: #191820;
        border-top: 1px solid #292631;
    }

    QSlider::groove:horizontal {
        height: 5px;
        background-color: #383342;
        border-radius: 2px;
    }

    QSlider::sub-page:horizontal {
        background-color: #A879FF;
        border-radius: 2px;
    }

    QSlider::handle:horizontal {
        background-color: #C9A7FF;
        width: 12px;
        margin: -4px 0;
        border-radius: 6px;
    }
    """