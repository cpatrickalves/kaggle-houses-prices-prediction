import os
import settings
from fastapi import FastAPI
import pandas as pd
from logzero import logger
import json
from src.models.predict import HousePriceModel
from src.api_models import PredictReponse
from src.models.predict import HousePriceModel
from typing import Dict
from datetime import datetime


app = FastAPI()
logger.info("API started")

@app.get("/")
def root():
    """
    Root view returns the system status
    """
    return {"status": "online"}


@app.post("/predict", response_model=PredictReponse)
def predict(inputs: dict):
    """Perform a prediction using data from a POST

    Args:
        inputs (json): input data in JSON format

    Returns:
        json: predict value as a JSON object
    """

    logger.info(f"API - POST /predict: \n {json.dumps(inputs, indent=4)}")

    # set the model saved at models/
    model_dir = 'tree_model'

    logger.info(f"Loading model: {model_dir}")
    model = HousePriceModel(model_dir)


    start = datetime.today()
    pred = model.predict(inputs)[0]
    dur = (datetime.today() - start).total_seconds()

    # Create response object
    response = PredictReponse(prediction=pred, duration=dur)


    return response
