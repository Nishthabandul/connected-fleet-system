from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class TelemetryData(BaseModel):
    vin: str                                      
    latitude: float                               
    longitude: float                              
    speed: float  
    engine_status: str                            
    fuel_level: float = Field(..., ge=0, le=100)  
    odometer: float                               
    diagnostic_codes: List[str] = []              
    timestamp: datetime          