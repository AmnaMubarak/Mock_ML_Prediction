from typing import Optional
from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse

from schema.predict import Item
from services.model import generate_prediction_id, mock_model_predict, results
from services.queue import q  # Import the queue

router = APIRouter()

# @router.post("/predict")
# def predict(item: Item):
#     output = mock_model_predict(item.input)
#     return output

@router.post("/predict")
async def predict(item: Item, background_tasks: BackgroundTasks, async_mode: Optional[bool] = True):
    if async_mode:
        prediction_id = generate_prediction_id()
        q.put((item.input, prediction_id))
        return JSONResponse(status_code=202, content={"message": "Request received. Processing asynchronously.", "prediction_id": prediction_id})

    else:
        output = mock_model_predict(item.input)
        return output
      
      
from fastapi.responses import JSONResponse

@router.get("/predict/{prediction_id}")
async def get_prediction(prediction_id: str):
    if prediction_id not in results:
        return JSONResponse(status_code=404, content={"error": "Prediction ID not found."})
    elif results[prediction_id] is None:
        return JSONResponse(status_code=400, content={"error": "Prediction is still being processed."})
    else:
        return JSONResponse(status_code=200, content={"prediction_id": prediction_id, "output": results[prediction_id]})     