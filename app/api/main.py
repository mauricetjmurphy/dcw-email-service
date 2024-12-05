from fastapi import APIRouter

from app.api.routes import health, message

api_router = APIRouter()
api_router.include_router(health.router, prefix="/mail", tags=["health"])
api_router.include_router(message.router, prefix="/mail", tags=["message"])
