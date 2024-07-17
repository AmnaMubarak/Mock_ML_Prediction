FROM python:3.10-slim-buster

# Set work directory
WORKDIR /app

# copy requirements to app directory
COPY ./requirements.txt /app/

# install requirements with no cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the application on port 8080
EXPOSE 8080

# Define the command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
