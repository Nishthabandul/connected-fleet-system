from pydantic import BaseModel
from datetime import datetime
class Alert(BaseModel):
    id: str               
    vin: str              
    type: str             
    severity: str         
    message: str         
    timestamp: datetime 