from fastapi import FastAPI, Query
from pydantic import BaseModel
import random


app = FastAPI()

class TemperatureResponse(BaseModel):
    location: str
    sensorId: str
    temperature: float

@app.get("/temperature/{sensor_id}", response_model=TemperatureResponse)
def get_temperature_by_sensor_id(sensor_id):
    temperature = random.randint(1, 100)
    return TemperatureResponse(location="default", sensorId=sensor_id, temperature=temperature)

@app.get("/temperature", response_model=TemperatureResponse)
def get_temperature(
    location: str = Query(..., description="Name of the room"),   
    ):
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

