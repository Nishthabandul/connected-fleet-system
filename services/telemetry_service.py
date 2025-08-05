from models.telemetry import TelemetryData
from storage.db import telemetry_db
from datetime import datetime, timedelta
from services.alert_service import generate_alert
def add_telemetry(data: TelemetryData):
    telemetry_db.setdefault(data.vin, []).append(data)
    # generate alerts based on telemetry conditions
    if data.speed > 120:
        generate_alert(
            vin=data.vin,
            type_="Speed",
            message=f"Speed exceeds 120 km/h: {data.speed} km/h",
            severity="High"
        )
    if data.fuel_level < 15:
        generate_alert(
            vin=data.vin,
            type_="Low Fuel",
            message=f"Fuel/Battery level is low: {data.fuel_level}%",
            severity="Medium"
        )
# Get latest telemetry data for a vehicle
def get_latest_telemetry(vin: str):
    return telemetry_db.get(vin, [])[-1] if vin in telemetry_db and telemetry_db[vin] else None

# Get full telemetry history 
def get_telemetry_history(vin: str):
    return telemetry_db.get(vin, [])