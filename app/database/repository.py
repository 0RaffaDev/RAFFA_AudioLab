
from app.database.connection import get_connection
from app.database.models import Media


class MediaRepository:

    def add(self, media):

        with get_connection() as connection:

            cursor = connection.execute("""
                INSERT INTO media (
                    name, file_path, media_type,
                    format, duration, sample_rate,
                    channels, category, is_favorite
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                media.name,
                media.file_path,
                media.media_type,
                media.format,
                media.duration,
                media.sample_rate,
                media.channels,
                media.category,
                int(media.is_favorite)
            ))

            return cursor.lastrowid

    def get_all(self, media_type=None):

        with get_connection() as connection:

            if media_type:
                cursor = connection.execute(
                    "SELECT * FROM media WHERE media_type = ?",
                    (media_type,)
                )
            else:
                cursor = connection.execute(
                    "SELECT * FROM media"
                )

            return [Media(
                id=row["id"],
                name=row["name"],
                file_path=row["file_path"],
                media_type=row["media_type"],
                format=row["format"],
                duration=row["duration"],
                sample_rate=row["sample_rate"],
                channels=row["channels"],
                category=row["category"],
                is_favorite=bool(row["is_favorite"])
            ) for row in cursor.fetchall()]

    def delete(self, media_id):

        with get_connection() as connection:
            connection.execute(
                "DELETE FROM media WHERE id = ?",
                (media_id,)
            )

    def set_favorite(self, media_id, favorite):

        with get_connection() as connection:
            connection.execute("""
                UPDATE media
                SET is_favorite = ?
                WHERE id = ?
            """, (int(favorite), media_id))
