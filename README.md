# Project Title

## Description

This is a Python project that uses FastAPI and Uvicorn for creating a web application. The project is organized as follows:

- `app/`: Contains the main application code.
  - `api/`: Contains the API endpoints.
  - `services/`: Contains services like model prediction and queue management.
  - `schema/`: Contains Pydantic models for request and response handling.
- `.vscode/`: Contains settings for the Visual Studio Code editor.
- `env/`: Contains the Python virtual environment.
- `dockerfile`: Contains instructions for building a Docker image of the application.
- `docker-compose.yml`: Used for defining and running Docker applications.

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
