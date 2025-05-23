# app/core/aws_clients.py

import boto3
from botocore.config import Config
from app.core.config import settings

# AWS configuration
aws_config = Config(
    region_name=settings.aws_region,
    retries={"max_attempts": 10, "mode": "standard"}
)

# Initialize clients
dynamodb_client = boto3.client("dynamodb", config=aws_config)
s3_client = boto3.client("s3", config=aws_config)
ses_client = boto3.client("ses", config=aws_config)

# Client access functions
def get_dynamodb_client():
    return dynamodb_client

def get_s3_client():
    return s3_client

def get_ses_client():
    return ses_client
