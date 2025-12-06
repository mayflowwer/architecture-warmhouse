from fastapi import FastAPI, Query
from pydantic import BaseModel
import random


app = FastAPI()

class TemperatureResponse(BaseModel):
    location: str
    sensorId: str
    temperature: float


@app.get("/temperature", response_model=TemperatureResponse)
def get_temperature(location: str = Query(..., description="Name of the room")):
    """
    Получает температуру по location. 
    Если location не распознан, sensorId = "0".
    """
    # Присваиваем sensorId по location
    if location == "Living Room":
        sensorId = "1"
    elif location == "Bedroom":
        sensorId = "2"
    elif location == "Kitchen":
        sensorId = "3"
    else:
        sensorId = "0"

    temperature = random.randint(1, 100)

    return TemperatureResponse(location=location, sensorId=sensorId, temperature=temperature)

