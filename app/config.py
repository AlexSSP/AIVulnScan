import os
from pathlib import Path
from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    ADMIN_USER: str = os.getenv("ADMIN_USER")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD")

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    MODEL_DIR: Path = BASE_DIR / "models"
    AI_MODEL_PATH: str = os.getenv("AI_MODEL_PATH", str(MODEL_DIR / "default_model.h5"))

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "")

    DATABASE_URL: AnyUrl = os.getenv("DATABASE_URL", "sqlite:///./scanner.db")

    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

    NVD_API_KEY: str = os.getenv("NVD_API_KEY", "")
    VIRUSTOTAL_API_KEY: str = os.getenv("VIRUSTOTAL_API_KEY", "")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()