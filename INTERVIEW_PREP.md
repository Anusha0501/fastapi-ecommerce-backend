# FastAPI Backend Interview Prep

## How to Explain This Project

Start with customer value: users browse products, add items to cart, and checkout safely. Then describe invariants: no negative inventory, no duplicate paid orders, secure authentication, and auditable order history.

## Senior-Level Talking Points

### 1. Problem

The business needs a backend that can handle product discovery, checkout, payment integration, and operational growth while preserving correctness.

### 2. Design

Use FastAPI for async HTTP APIs, PostgreSQL for transactional data, Redis for cache/session/rate limiting, and a message broker for asynchronous side effects.

### 3. Alternatives

- REST is simple and widely understood; GraphQL can reduce over-fetching for complex catalog pages.
- JWT is stateless; server-side sessions are easier to revoke.
- Optimistic locking scales well; pessimistic locking is safer for high-contention inventory.

### 4. Interview Questions and Model Answers

#### How do you prevent duplicate orders?

Require an `Idempotency-Key` header for checkout. Store the key with the user ID, request hash, and final response. If the same request is retried, return the original response instead of creating another order.

#### How do you prevent overselling?

Use an atomic SQL update such as `UPDATE inventory SET available = available - :qty WHERE sku = :sku AND available >= :qty`. If no row is updated, reject checkout or backorder according to business rules.

#### How do you handle payment webhooks?

Verify provider signatures, process events idempotently, persist the raw event for audit, and transition order state only through valid transitions.

#### How do you scale reads?

Cache product detail pages, add read replicas for catalog queries, denormalize search documents into a search engine, and paginate all list endpoints.

### 5. Tradeoffs

- Idempotency storage adds complexity but is mandatory for payment safety.
- Atomic inventory updates are simple but can create hot rows for popular SKUs.
- JWT tokens reduce DB lookups but complicate immediate revocation.

## Practice Prompts

1. Design checkout for 10,000 requests per second.
2. Design product search with filters and sorting.
3. Design refund and partial refund workflows.
4. Design admin audit logging.
5. Design rate limiting for login and checkout.
