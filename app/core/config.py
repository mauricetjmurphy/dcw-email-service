from pydantic import EmailStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    aws_region: str = "us-east-1"
    ses_verified_email: EmailStr = "mauricetjmurphy@gmail.com"  # Verified sender email
    private_email: EmailStr = "mauricetjmurphy@gmail.com"       # Your private email for receiving messages

class Config:
        env_file = ".env"

settings = Settings()
