import os
from pathlib import Path


class Settings:
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_DIR = BASE_DIR / "models"

    AI_MODEL_PATH: str = os.getenv("AI_MODEL_PATH", str(MODEL_DIR / "default_model.h5"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    MODEL_CACHE_SIZE: int = int(os.getenv("MODEL_CACHE_SIZE", 1))


settings = Settings()