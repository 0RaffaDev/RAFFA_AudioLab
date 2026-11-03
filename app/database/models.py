
from dataclasses import dataclass


@dataclass
class Media:
    name: str
    file_path: str
    media_type: str
    format: str = None
    duration: float = None
    sample_rate: int = None
    channels: int = None
    category: str = None
    is_favorite: bool = False
    id: int = None
