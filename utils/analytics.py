from storage.db import vehicles_db, telemetry_db, alerts_db
from datetime import datetime, timedelta

def get_analytics_summary():
    now = datetime.utcnow()
    inactive_threshold = now - timedelta(hours=24)

    active_count = 0
    inactive_count = 0
    total_fuel = 0
    fuel_count = 0
    total_distance = 0

    for vin, vehicle in vehicles_db.items():
        telemetry_list = telemetry_db.get(vin, [])
        
        if telemetry_list:
            latest = telemetry_list[-1]
            if latest.timestamp < inactive_threshold:
                inactive_count += 1
            else:
                active_count += 1

            total_fuel += latest.fuel_level
            fuel_count += 1

            # Calculate distance covered in last 24 hours
            recent = [t for t in telemetry_list if t.timestamp >= inactive_threshold]
            if len(recent) >= 2:
                
                distance = recent[-1].odometer - recent[0].odometer
                if distance > 0:
                    total_distance += distance
        else:
            inactive_count += 1

    avg_fuel_level = (total_fuel / fuel_count) if fuel_count else 0

    # Count alerts 
    alert_summary = {}
    for alert in alerts_db.values():
        key = f"{alert.type} | {alert.severity}"
        alert_summary[key] = alert_summary.get(key, 0) + 1

    return {
        "active_vehicles": active_count,
        "inactive_vehicles": inactive_count,
        "average_fuel_level": round(avg_fuel_level, 2),
        "total_distance_last_24h": round(total_distance, 2),
        "alert_summary": alert_summary
    }
