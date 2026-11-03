
from app.database.connection import initialize_database
from app.core.library_manager import LibraryManager

initialize_database()

biblioteca = LibraryManager()

resultado, mensaje = biblioteca.importar_archivo(
    r"C:\Users\gonza\Music\Nebuleo - Xanti x prodRAFFA.mp3",
    "song"
)

print(mensaje)

canciones = biblioteca.repository.get_all("song")

for cancion in canciones:
    print(cancion.name, cancion.format)

cantidad = biblioteca.importar_carpeta(
    r"C:\Users\gonza\Music",
    "song"
)

print(f"Se importaron {cantidad} archivos.")