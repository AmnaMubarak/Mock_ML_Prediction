import queue
import time
import random
from typing import Dict
import uuid

results = {}   

def mock_model_predict(input: str, prediction_id: str) -> None:
    time.sleep(random.randint(8, 15))  # Simulate processing delay
    result = str(random.randint(100, 10000))
    output = {"input": input, "result": result}
    results[prediction_id] = output
  

def generate_prediction_id():
    return str(uuid.uuid4())  
  