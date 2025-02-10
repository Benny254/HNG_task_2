FastAPI Application Deployment with CI/CD

Project Overview

This project deploys a FastAPI application with a Continuous Integration (CI) and Continuous Deployment (CD) pipeline. It includes an additional API endpoint to retrieve book details by ID and is served using Nginx as a reverse proxy.

Resources

FastAPI Book Project Template: GitHub Repository

FastAPI Documentation: FastAPI Docs

Nginx Documentation: Nginx Docs

GitHub Actions Documentation: GitHub Actions Docs

Project Setup

1. Clone the Repository

Fork the template repository and clone it locally:

 git clone https://github.com/your-username/fastapi-book-project.git
 cd fastapi-book-project

2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application Locally

uvicorn app.main:app --reload

The application should be accessible at http://127.0.0.1:8000.

Implementing the Missing Endpoint

Endpoint Details

Method: GET

URL: /api/v1/books/{book_id}

Functionality:

Retrieve a book by its ID.

Return a JSON response with book details.

Return 404 Not Found if the book does not exist.

Example Response

Success (200 OK):

{
    "id": 1,
    "title": "Example Book",
    "author": "John Doe"
}

Failure (404 Not Found):

{
    "detail": "Book not found"
}

CI/CD Pipeline Setup

1. CI Pipeline (Testing)

Trigger: Runs on pull requests to the main branch.

Job Name: test

Actions:

Run pytest to test the API.

Fail if any tests fail.

2. CD Pipeline (Deployment)

Trigger: Runs when a pull request is merged into main.

Job Name: deploy

Actions:

Automatically deploy the latest changes.

Deployment with Nginx

1. Install and Configure Nginx

sudo apt update && sudo apt install nginx

Edit the Nginx configuration file:

sudo nano /etc/nginx/sites-available/default

Add the following content:

server {
    listen 80;
    server_name your_domain_or_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Restart Nginx:

sudo systemctl restart nginx

Repository Access Requirement

Invite the hng12-devbotops GitHub account as a collaborator before submission.

Submission Guidelines

Submit your solution in the #stage-two-backend Slack channel using the /submit command. Include:

The base URL of your deployed application.

Your GitHub repository URL.

Submission Deadline

12th February 2025, 11:59 PM WAT (GMT +1).

Late submissions will not be accepted.

Evaluation Criteria

Your submission will be evaluated based on:

Correct implementation of the API endpoint.

Proper setup of CI/CD pipelines.

Successful deployment with Nginx integration.