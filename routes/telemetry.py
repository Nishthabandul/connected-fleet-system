from fastapi import APIRouter, HTTPException
from models.telemetry import TelemetryData
from services.telemetry_service import (
    add_telemetry,
    get_telemetry_history,
    get_latest_telemetry
)
from utils.analytics import get_analytics_summary

router = APIRouter(prefix="/telemetry", tags=["Telemetry"])


@router.post("/")
def receive_telemetry(data: TelemetryData):
    add_telemetry(data)
    return {"message": "Telemetry data received successfully"}


@router.get("/analytics/summary")
def get_analytics():
    return get_analytics_summary()


@router.get("/{vin}/latest")
def get_latest_vehicle_telemetry(vin: str):
    data = get_latest_telemetry(vin)
    if not data:
        raise HTTPException(status_code=404, detail="No telemetry found for this vehicle")
    return data


@router.get("/{vin}")
def get_vehicle_telemetry_history(vin: str):
    data = get_telemetry_history(vin)
    if not data:
        raise HTTPException(status_code=404, detail="No telemetry found for this vehicle")
    return data
