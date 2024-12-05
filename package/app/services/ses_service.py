from app.core.aws_clients import get_ses_client
from app.core.config import settings

ses_client = get_ses_client()

def send_user_message(name: str, user_email: str,user_phone:str, message: str, budget: str):
    """Send an email with the user's message to your private email."""
    subject = f"New Message from Documated"
    body = f"Name: {name}\nEmail: {user_email}\nPhone: {user_phone}\nBudget: {budget}\n\nMessage:\n{message}"
    
    # Send the email using SES
    ses_client.send_email(
        Source=settings.ses_verified_email,
        Destination={
            "ToAddresses": [settings.private_email]
        },
        Message={
            "Subject": {
                "Data": subject
            },
            "Body": {
                "Text": {
                    "Data": body
                }
            }
        }
    )
