# MOCK ML PREDICTIONS

## Description

This is a Python project that uses FastAPI and Uvicorn for creating a web application.





The project is organized as follows:

- `app/`: Contains the main application code.
  - `api/`: Contains the API endpoints.
  - `services/`: Contains services like model prediction and queue management.
  - `schema/`: Contains Pydantic models for request and response handling.
- `.vscode/`: Contains settings for the Visual Studio Code editor.
- `env/`: Contains the Python virtual environment.
- `dockerfile`: Contains instructions for building a Docker image of the application.
- `docker-compose.yml`: Used for defining and running Docker applications.

## Business Logic

The application provides a machine learning prediction service with the following capabilities:

- **Prediction Endpoints**: The API offers both synchronous and asynchronous prediction modes
  - `POST /predictions/predict`: Submit input for prediction
  - `GET /predictions/predict/{prediction_id}`: Retrieve results for asynchronous predictions
  
- **Processing Queue**: Asynchronous predictions are managed through a background queue system
  - Predictions are processed in the background while immediately returning a prediction ID
  - Clients can check the status of predictions using the prediction ID
  
- **Mock Model**: The service currently uses a mock model that:
  - Simulates processing time (8-15 seconds)
  - Returns randomized prediction results
  - Demonstrates the asynchronous processing architecture

- **Health Check**: A root endpoint (`/`) provides basic application health status

This architecture allows for high throughput by processing prediction requests asynchronously, which is particularly valuable for ML models with longer inference times.

## Getting Started

### Prerequisites

- Python 3.10.1
- Docker Desktop (if you want to run the application in a container)

### Installation

1. Clone the repository.
2. Create a Python virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.

### Running the Application

You can run the application using docker-compose command.

```sh
docker-compose up --build
