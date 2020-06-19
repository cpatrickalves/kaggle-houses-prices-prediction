import os
import settings
from fastapi import FastAPI
import pandas as pd
from logzero import logger
from pydantic import BaseModel
from typing import Dict
import json
from src.models.predict import HousePriceModel


app = FastAPI()

logger.info("API started")

@app.get("/")
def root():
    """
    Root view returns the system status
    """
    return {"status": "online"}


@app.post("/predict")
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

    response = {"Prediction": model.predict(inputs)[0]}

    return response
