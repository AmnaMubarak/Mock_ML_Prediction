
import queue
from threading import Thread

from services.model import mock_model_predict
# Create a Queue instance
q = queue.Queue()

# Function to process tasks from the queue
def process_queue():
    while True:
        task = q.get()
        if task is None:
            break
        mock_model_predict(*task)
        q.task_done()
        
# Start a background thread to process tasks from the queue
Thread(target=process_queue, daemon=True).start()     