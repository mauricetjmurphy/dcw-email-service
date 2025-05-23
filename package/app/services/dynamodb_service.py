from app.core.aws_clients import get_dynamodb_client

dynamodb_client = get_dynamodb_client()

def create_user_in_dynamodb(user_id: str, user_data: dict):
    """Create a user in DynamoDB."""
    table_name = "users"
    dynamodb_client.put_item(
        TableName=table_name,
        Item={
            "user_id": {"S": user_id},
            "user_data": {"S": str(user_data)}
        }
    )

def get_user_from_dynamodb(user_id: str):
    """Retrieve a user from DynamoDB."""
    table_name = "users"
    response = dynamodb_client.get_item(
        TableName=table_name,
        Key={"user_id": {"S": user_id}}
    )
    return response.get("Item")
