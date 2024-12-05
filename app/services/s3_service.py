from app.core.aws_clients import get_s3_client

s3_client = get_s3_client()

def upload_file_to_s3(bucket_name: str, object_key: str, file_data: bytes):
    """Upload a file to S3."""
    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=file_data)
    return f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

def get_file_url_from_s3(bucket_name: str, object_key: str):
    """Generate a URL for accessing a file in S3."""
    return f"https://{bucket_name}.s3.amazonaws.com/{object_key}"

