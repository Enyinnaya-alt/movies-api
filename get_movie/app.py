import boto3
import json
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')  # Replace 'Movies' with your DynamoDB table name

def lambda_handler(event, context):
    # Extract movie ID from the path parameters
    movie_id = event['pathParameters']['movieId']

    # Query DynamoDB for the movie
    response = table.query(
        KeyConditionExpression=Key('id').eq(movie_id)
    )

    # Check if the movie exists
    if 'Items' in response and response['Items']:
        return {
            "statusCode": 200,
            "body": json.dumps(response['Items'][0])
        }

    # Return a 404 error if the movie is not found
    return {
        "statusCode": 404,
        "body": json.dumps({"error": "Movie not found"})
    }