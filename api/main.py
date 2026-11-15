from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI()
readings = []

class Reading(BaseModel):
    device_id: str
    temperature_c: float

@app.get("/health")
def greet():
    return {"status" : "ok"}

@app.post("/reading")
def add_reading(reading : Reading):
    record = {
    "device_id": reading.device_id,
    "temperature_c": reading.temperature_c,
    "received_at": datetime.now(timezone.utc).isoformat(),
    }
    readings.append(record)

@app.get("/reading")
def list_readings():
    return readings
