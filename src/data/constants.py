from pathlib import Path

PARENT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PARENT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

SUPPORTED_DOMAINS = [
    "movie",
    "books",
    "music"
]