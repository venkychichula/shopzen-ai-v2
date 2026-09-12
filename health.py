from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz")
def healthz():
    return {
        "ok": True,
        "service": "shopzen-ai-v2",
        "version": "2.0.0",
    }

@router.get("/api")
def api_info():
    return {
        "name": "ShopZen AI V2",
        "status": "online",
        "phase": "foundation",
    }
