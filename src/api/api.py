from fastapi import FastAPI
import pandas as pd
from logzero import logger

# ------------------------ HOW TO USE ------------------------ #
# To see API documentation, start the API and access:
# <IPADDRESS>:8000/docs
# or
# <IPADDRESS>:8000/redoc
# or
# <IPADDRESS>:8000/openapi.json

app = FastAPI()

@app.get("/")
def api_status():
    """
    Root view returns the system status
    """
    return {"status": "online"}

