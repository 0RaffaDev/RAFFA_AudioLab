
from pathlib import Path

from app.database.models import Media
from app.database.repository import MediaRepository


class LibraryManager:

    FORMATOS_COMPATIBLES = {
        ".mp3",
        ".wav",
        ".flac",
        ".ogg",
        ".m4a",
        ".aac",
        ".wma"
    }

    def __init__(self):
        self.repository = MediaRepository()

    def importar_archivo(self, file_path, media_type):

        archivo = Path(file_path).resolve()

        if not archivo.exists() or not archivo.is_file():
            return False, "El archivo no existe."

        if archivo.suffix.lower() not in self.FORMATOS_COMPATIBLES:
            return False, "Formato de audio no compatible."

        if media_type not in ("song", "sample"):
            return False, "Tipo de archivo inválido."

        # Evitar importar archivos repetidos
        archivos_guardados = self.repository.get_all()

        for media in archivos_guardados:
            if Path(media.file_path).resolve() == archivo:
                return False, "Este archivo ya está en la biblioteca."

        nuevo_media = Media(
            name=archivo.stem,
            file_path=str(archivo),
            media_type=media_type,
            format=archivo.suffix.replace(".", "").upper()
        )

        self.repository.add(nuevo_media)

        return True, "Archivo importado correctamente."

    def importar_carpeta(self, folder_path, media_type):

        carpeta = Path(folder_path)

        if not carpeta.exists() or not carpeta.is_dir():
            return 0

        cantidad_importada = 0

        for archivo in carpeta.rglob("*"):

            if archivo.is_file():

                resultado, mensaje = self.importar_archivo(
                    archivo,
                    media_type
                )

                if resultado:
                    cantidad_importada += 1

        return cantidad_importada
