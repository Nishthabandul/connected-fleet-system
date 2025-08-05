from fastapi import FastAPI
from routes.vehicles import router as vehicles_router
from routes.telemetry import router as telemetry_router
from routes.alerts import router as alerts_router

app = FastAPI(title="Connected Car Fleet Management System")

# Include routers with appropriate prefixes and tags
app.include_router(vehicles_router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(telemetry_router, prefix="/telemetry", tags=["Telemetry"])
app.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Fleet management API is running"}
