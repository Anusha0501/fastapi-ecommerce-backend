import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Settings:
    app_name: str = "FastAPI E-commerce Backend"
    api_version: str = "0.1.0"
    environment: str = "local"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ecommerce"
    jwt_secret_key: str = "change-me-in-production"


@lru_cache
def get_settings() -> Settings:
    return Settings(
        app_name=os.getenv("APP_NAME", Settings.app_name),
        api_version=os.getenv("API_VERSION", Settings.api_version),
        environment=os.getenv("ENVIRONMENT", Settings.environment),
        database_url=os.getenv("DATABASE_URL", Settings.database_url),
        jwt_secret_key=os.getenv("JWT_SECRET_KEY", Settings.jwt_secret_key),
    )


settings = get_settings()
