from pydantic import BaseModel
from typing import Optional

class Vehicle(BaseModel):
    vin: str  # Vehicle Identification Number
    manufacturer: str
    model: str
    fleet_id: str  # Corporate, Rental, Personal
    owner: str
    operator: str
    registration_status: str  # Active, Maintenance, Decommissioned
