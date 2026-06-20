import pytest

from app.core.config import get_settings
from app.domain.catalog import get_product_by_slug, list_active_products
from app.domain.products import ProductVariant


def test_default_settings_are_available_without_external_dependencies() -> None:
    settings = get_settings()

    assert settings.app_name == "FastAPI E-commerce Backend"
    assert settings.environment == "local"


def test_list_active_products_returns_seed_catalog() -> None:
    products = list_active_products()

    assert len(products) == 1
    assert products[0].slug == "classic-tee"
    assert products[0].variants[0].sku == "TEE-BLK-M"


def test_get_product_by_slug_returns_none_for_unknown_product() -> None:
    assert get_product_by_slug("missing") is None


def test_product_variant_rejects_negative_price() -> None:
    with pytest.raises(ValueError, match="price_cents"):
        ProductVariant(sku="BAD-SKU", price_cents=-1)
