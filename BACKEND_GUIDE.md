# Backend Engineering Guide

## 1. Problem

A production backend needs more than endpoint implementation. It must enforce business invariants, protect customer data, tolerate dependency failures, be observable, and remain understandable as the team grows.

## 2. Design

### Recommended FastAPI Structure

```text
app/
  main.py
  api/v1/routes/
  core/config.py
  core/security.py
  domain/
  infrastructure/
  tests/
```

### Engineering Standards

- Use Pydantic schemas at API boundaries.
- Use SQLAlchemy models for persistence, not as domain objects in complex flows.
- Keep route handlers thin.
- Use service classes for business workflows.
- Use repositories/adapters for external systems.
- Enforce formatting, typing, and tests in CI.

### Error Handling

Return consistent error bodies:

```json
{
  "code": "inventory_unavailable",
  "message": "One or more items are unavailable",
  "details": {"sku": "TSHIRT-BLACK-M"}
}
```

### Observability

- Structured JSON logs with request IDs.
- Metrics for request latency, checkout failures, payment errors, and DB latency.
- Distributed traces across API, database, cache, and payment provider calls.

## 3. Alternatives

- Function-based services are simple, but class-based services make dependency injection clearer.
- Active Record is fast to build, but repository patterns isolate persistence decisions.
- BackgroundTasks are easy, but a broker-backed worker is safer for production side effects.

## 4. Interview Questions

1. Why should route handlers stay thin?
2. How does dependency injection help testability?
3. What belongs in middleware versus service logic?
4. How do you design a retry policy safely?
5. What is the difference between authentication and authorization?

## 5. Tradeoffs

- More layers add ceremony but improve long-term maintainability.
- Strict typing costs time upfront but catches integration bugs earlier.
- Centralized error handling improves consistency but requires disciplined exception design.
