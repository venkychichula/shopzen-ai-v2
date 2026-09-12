from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.config import settings
from backend.routes.health import router as health_router
from backend.routes.chat import router as chat_router

app = FastAPI(
    title="ShopZen AI V2",
    version="2.0.0",
    description="Modular AI shopping assistant foundation."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
