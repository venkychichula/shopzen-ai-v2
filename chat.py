from fastapi import APIRouter
from pydantic import BaseModel, Field
from backend.services.ai import ask_ai

router = APIRouter(prefix="/api/chat", tags=["AI"])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

@router.post("")
def chat(req: ChatRequest):
    return ask_ai(req.message)
