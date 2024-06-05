from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request
from schema.predict import Item
from services.model import mock_model_predict

from api.endpoints import (
    predictions
)
api_router = APIRouter()

@api_router.get("/", response_class=JSONResponse)
async def ping():
    """
    This function is used for health check of the application.
    """
    return {
        "message": "Application is Running!",
        "status": "success"
    }

api_router.include_router(predictions.router, prefix="/predictions", tags=["predict"])
