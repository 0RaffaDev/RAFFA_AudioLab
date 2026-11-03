
import sqlite3
from pathlib import Path


# Ubicación de la base de datos
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "audiolab.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    with get_connection() as connection:

        connection.execute("""
            CREATE TABLE IF NOT EXISTS media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                file_path TEXT NOT NULL UNIQUE,
                media_type TEXT NOT NULL
                    CHECK(media_type IN ('song', 'sample')),
                format TEXT,
                duration REAL,
                sample_rate INTEGER,
                channels INTEGER,
                category TEXT,
                is_favorite INTEGER DEFAULT 0,
                date_added TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
