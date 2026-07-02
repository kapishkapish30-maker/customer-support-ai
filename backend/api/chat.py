from fastapi import APIRouter
from pydantic import BaseModel

from agents.router import route_query

router = APIRouter()

class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    reply = route_query(request.message)
    return {
        "reply": reply
    }