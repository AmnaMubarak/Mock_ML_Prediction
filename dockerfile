# select docker image of uvicorn-gunicorn-fastapi with python 3.10
# By default this image runs gunicorn on port 80 and with uvicorn.workers.UvicornWorker
# By default max workers are unlimited
FROM python:3.10-slim-buster

# Set work directory
WORKDIR /app

# copy requirements to app directory
COPY ./requirements.txt /app/

# install requirements with no cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy code
COPY ./app /app

# Expose the application on port 8000
EXPOSE 8080

# Define the command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]