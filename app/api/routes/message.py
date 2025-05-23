import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.services.ses_service import send_user_message
from app.models.message import MessageSchema

# Initialize the logger
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/send-message")
async def send_message(data: MessageSchema):
    """Endpoint for users to send messages via contact form."""
    try:
        send_user_message(name=data.name, user_email=data.email, user_phone=data.phone, message=data.message, budget=data.budget)
        return {"message": "Your message has been sent successfully."}
    except Exception as e:
       # Log the error
        logger.error(f"Error sending message from {data.email}: {e}")
        raise HTTPException(status_code=500, detail="Failed to send the message. Please try again later.")
