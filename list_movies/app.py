import boto3
import json

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')  # Replace 'Movies' with your DynamoDB table name

def lambda_handler(event, context):
    # Scan the entire table to retrieve all movies
    response = table.scan()

    # Return the list of movies
    return {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    }