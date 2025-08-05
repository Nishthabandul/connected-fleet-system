from models.alert import Alert
from storage.db import alerts_db
from datetime import datetime
import uuid

def generate_alert(vin: str, type_: str, message: str, severity: str):
    alert_id = str(uuid.uuid4())
    alert = Alert(
        id=alert_id,
        vin=vin,
        type=type_,
        severity=severity,
        message=message,
        timestamp=datetime.utcnow()
    )
    alerts_db[alert_id] = alert
    return alert

def get_all_alerts():
    return list(alerts_db.values())

def get_alert_by_id(alert_id: str):
    return alerts_db.get(alert_id)
