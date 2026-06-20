from dataclasses import dataclass, field


@dataclass(frozen=True)
class ProductVariant:
    sku: str
    price_cents: int
    currency: str = "USD"
    available: int = 0

    def __post_init__(self) -> None:
        if self.price_cents < 0:
            raise ValueError("price_cents must be greater than or equal to zero")
        if self.available < 0:
            raise ValueError("available must be greater than or equal to zero")


@dataclass(frozen=True)
class Product:
    slug: str
    name: str
    description: str
    active: bool = True
    variants: list[ProductVariant] = field(default_factory=list)
