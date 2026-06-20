# API Design

## 1. Problem

The API must expose predictable contracts to web, mobile, and admin clients while protecting sensitive operations such as checkout, payment, and inventory management.

## 2. Design

### API Principles

- Version routes under `/api/v1`.
- Use nouns for resources and verbs only for workflow actions.
- Require authentication for carts, checkout, orders, and admin APIs.
- Use pagination for list endpoints.
- Use idempotency keys for checkout and payment-adjacent operations.

### Endpoint Sketch

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/api/v1/auth/register` | Create account |
| `POST` | `/api/v1/auth/login` | Issue token |
| `GET` | `/api/v1/products` | List products |
| `GET` | `/api/v1/products/{slug}` | Product detail |
| `POST` | `/api/v1/cart/items` | Add item |
| `PATCH` | `/api/v1/cart/items/{item_id}` | Update quantity |
| `POST` | `/api/v1/checkout` | Create order from cart |
| `GET` | `/api/v1/orders` | User order history |
| `POST` | `/api/v1/webhooks/payments` | Payment webhook |

### Checkout Request

```http
POST /api/v1/checkout
Idempotency-Key: 01JABC...
Authorization: Bearer <token>
```

```json
{
  "shipping_address_id": "addr_123",
  "payment_method_id": "pm_123"
}
```

### Checkout Response

```json
{
  "order_id": "ord_123",
  "status": "paid",
  "total_cents": 12999,
  "currency": "USD"
}
```

## 3. Alternatives

- GraphQL can support flexible catalog screens but complicates caching and authorization.
- RPC-style endpoints are clear for workflows but can become inconsistent for CRUD resources.
- Cursor pagination is better for large datasets; offset pagination is simpler for small admin views.

## 4. Interview Questions

1. Why version APIs?
2. How do you design pagination?
3. What should be idempotent?
4. How should API errors be structured?
5. How do you protect admin endpoints?

## 5. Tradeoffs

- Strict contracts slow rapid prototyping but prevent client breakage.
- Idempotency keys require persistence but make retries safe.
- Cursor pagination is robust but harder for clients than page numbers.
