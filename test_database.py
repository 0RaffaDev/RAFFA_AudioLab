
from app.database.connection import initialize_database
from app.database.models import Media
from app.database.repository import MediaRepository


# Inicializar base de datos
initialize_database()

repository = MediaRepository()

# Registrar una canción de prueba
cancion = Media(
    name="Mi primera canción",
    file_path="C:/Musica/primera_cancion.wav",
    media_type="song",
    format="WAV",
    duration=180.5,
    sample_rate=44100,
    channels=2
)

repository.add(cancion)

# Consultar canciones
canciones = repository.get_all("song")

for cancion in canciones:
    print(cancion)
