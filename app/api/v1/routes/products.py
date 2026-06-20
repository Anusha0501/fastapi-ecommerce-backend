from fastapi import APIRouter, HTTPException, status

from app.domain.catalog import get_product_by_slug, list_active_products
from app.domain.products import Product

router = APIRouter()


@router.get("", response_model=list[Product])
def list_products() -> list[Product]:
    return list_active_products()


@router.get("/{slug}", response_model=Product)
def get_product(slug: str) -> Product:
    product = get_product_by_slug(slug)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
