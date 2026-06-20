from fastapi import FastAPI

from app.api.v1.routes import health, products
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        description="Production-grade e-commerce backend reference implementation.",
    )
    app.include_router(health.router, tags=["health"])
    app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
    return app


app = create_app()
