# Movies API - Serverless

This project provides a serverless API to manage movie information using AWS Lambda, API Gateway, and DynamoDB.

## Features
- **Get Movie Details**: Retrieve details of a specific movie by ID.
- **List All Movies**: Retrieve a list of all movies.

## Architecture
- **API Gateway**: Exposes RESTful endpoints.
- **AWS Lambda**: Handles API requests.
- **DynamoDB**: Stores movie data.

## Endpoints
- `GET /movies/{movieId}`: Get details of a movie by ID.
- `GET /movies`: List all movies.

## Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/Enyinnaya-alt/movies-api-serverless.git
   cd movies-api-serverless
