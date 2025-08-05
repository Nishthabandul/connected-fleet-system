from fastapi import APIRouter, HTTPException
from services.alert_service import get_all_alerts, get_alert_by_id

router = APIRouter(prefix="/alerts", tags=["Alerts"])

# Get all alerts
@router.get("/")
def fetch_all_alerts():
    return get_all_alerts()

# Get a specific alert by ID
@router.get("/{alert_id}")
def fetch_alert_by_id(alert_id: str):
    alert = get_alert_by_id(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert
