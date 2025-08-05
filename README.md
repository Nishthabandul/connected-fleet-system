# Connected Car Fleet Management System

The Connected Car Fleet Management System is a backend application built using **FastAPI**. It provides a complete set of RESTful APIs to manage a fleet of connected vehicles, collect and analyze real-time telemetry data, and perform fleet-wide analytics.

This system is ideal for fleet operators, logistics companies, and researchers exploring IoT-based vehicle monitoring systems.

---

##  Key Features

* **Vehicle Management**
  Add, view, and remove vehicles from the fleet using a VIN (Vehicle Identification Number) as the unique key.

* **Telemetry Data Collection**
  Accepts real-time data like GPS coordinates, speed, engine status, fuel levels, and error codes.

* **Telemetry History & Latest View**
  Easily retrieve all historical telemetry data or just the latest update for any vehicle.

* **Fleet Analytics**
  View summarized insights such as:

  * Active vs. inactive vehicles
  * Average fuel levels
  * Total distance covered in the last 24 hours
  * Diagnostic code trends

* **Alerts (Extensible)**
  Infrastructure in place to integrate real-time alerts for abnormal vehicle conditions.

---

## 🗂️ Project Structure

```
connectedfleet2/
├── main.py                    # App entry point
├── models/                    # Pydantic models for Vehicle, Telemetry, Alert
│   ├── vehicle.py
│   ├── telemetry.py
│   └── alert.py
├── routes/                    # API route definitions
│   ├── vehicles.py
│   ├── telemetry.py
│   └── alerts.py
├── services/                  # Business logic
│   ├── vehicle_service.py
│   ├── telemetry_service.py
│   └── alert_service.py
├── utils/                     # Utility functions
│   └── analytics.py
├── storage/                   # In-memory data store (can be replaced with DB)
│   └── db.py
└── requirements.txt           # Python dependencies
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nishthabandul/connected-fleet-system.git
cd connected-fleet-system
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI App

```bash
uvicorn main:app --reload
```

The app will run at:
`http://127.0.0.1:8000`

---

## 📘 API Documentation

FastAPI provides interactive Swagger UI documentation by default.

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc UI:** `http://127.0.0.1:8000/redoc`

Use these interfaces to test the following endpoints:

### Vehicle Endpoints

* `GET /vehicles/vehicles/` – List all vehicles
* `POST /vehicles/vehicles/` – Add a new vehicle
* `GET /vehicles/vehicles/{vin}` – Get vehicle details
* `DELETE /vehicles/vehicles/{vin}` – Remove a vehicle

### Telemetry Endpoints

* `POST /telemetry/telemetry/` – Send new telemetry data
* `GET /telemetry/telemetry/{vin}` – Get telemetry history for a vehicle
* `GET /telemetry/telemetry/{vin}/latest` – Get latest telemetry
* `GET /telemetry/telemetry/analytics/summary` – Get fleet-wide analytics

---

## 🧪 Example Payloads

### Add a Vehicle

```json
{
  "vin": "ABC1234567",
  "manufacturer": "Tata Motors",
  "model": "Nexon EV",
  "fleet_id": "fleet_001",
  "owner": "Nishtha Bandul",
  "operator": "Tata Fleet Ops",
  "registration_status": "Registered"
}
```

### Send Telemetry Data

```json
{
  "vin": "ABC1234567",
  "latitude": 28.6139,
  "longitude": 77.2090,
  "speed": 80,
  "engine_status": "on",
  "fuel_level": 45.5,
  "odometer": 12034.7,
  "diagnostic_codes": ["P0123", "P0456"],
  "timestamp": "2025-08-05T14:30:00"
}
```

---

## 🗃️ Data Storage

Currently, this project uses **in-memory storage** via Python dictionaries defined in `storage/db.py`.

If the server restarts, all data will be lost. You can upgrade to persistent storage by integrating:

* **PostgreSQL** or **SQLite** with SQLAlchemy
* **MongoDB** using Motor
* **Redis** for real-time queues and alerts


## Future Enhancements

* Add database integration (PostgreSQL/MongoDB)
* Build frontend dashboard for monitoring
* Integrate WebSockets for real-time alerts
* Role-based authentication and admin login
* Add support for push notifications or SMS for critical issues

Contributing

Feel free to fork the repo and contribute. If you'd like to suggest features or report bugs, open an issue or submit a pull request.

License

This project is licensed under the **MIT License**.


