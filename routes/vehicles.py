# routes/vehicles.py

from fastapi import APIRouter, HTTPException
from models.vehicle import Vehicle
from services.vehicle_service import (
    create_vehicle,
    get_all_vehicles,
    get_vehicle_by_vin,
    delete_vehicle
)

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.post("/")
def add_vehicle(vehicle: Vehicle):
    return create_vehicle(vehicle)

@router.get("/")
def list_vehicles():
    return get_all_vehicles()

@router.get("/{vin}")
def get_vehicle(vin: str):
    vehicle = get_vehicle_by_vin(vin)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{vin}")
def remove_vehicle(vin: str):
    deleted = delete_vehicle(vin)
    if not deleted:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"message": "Vehicle deleted successfully"}
