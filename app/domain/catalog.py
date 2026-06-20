from app.domain.products import Product, ProductVariant

SAMPLE_PRODUCTS: dict[str, Product] = {
    "classic-tee": Product(
        slug="classic-tee",
        name="Classic Tee",
        description="Soft cotton t-shirt for everyday wear.",
        variants=[ProductVariant(sku="TEE-BLK-M", price_cents=2500, available=100)],
    )
}


def list_active_products() -> list[Product]:
    return [product for product in SAMPLE_PRODUCTS.values() if product.active]


def get_product_by_slug(slug: str) -> Product | None:
    return SAMPLE_PRODUCTS.get(slug)
