# ShopZen AI V2

A clean, modular rebuild of ShopZen AI.

## Current phase

**V2.0 Foundation**

- FastAPI backend
- Modular backend structure
- Environment-based secrets
- Render configuration
- `/healthz` health check
- AI chat service with Groq
- Separate frontend assets
- No hard-coded API keys

## Run locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Create `.env` from `.env.example`, add `GROQ_API_KEY`, then:

```bash
uvicorn app:app --reload
```

Open:

`http://127.0.0.1:8000`

## Deployment

Render can use:

- Build: `pip install -r requirements.txt`
- Start: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- Health check: `/healthz`

## Roadmap

1. Product intelligence
2. Retailer engine
3. Price intelligence
4. Search and recommendation pipeline
5. Authentication and persistence
6. Wishlist and history
7. Review intelligence
8. Shopping rooms
9. Observability and production hardening
