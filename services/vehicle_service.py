# services/vehicle_service.py

from models.vehicle import Vehicle
from storage.db import vehicles_db

def create_vehicle(vehicle: Vehicle):
    vehicles_db[vehicle.vin] = vehicle
    return vehicle

def get_all_vehicles():
    return list(vehicles_db.values())

def get_vehicle_by_vin(vin: str):
    return vehicles_db.get(vin)

def delete_vehicle(vin: str):
    return vehicles_db.pop(vin, None)
