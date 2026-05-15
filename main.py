from fastapi import FastAPI
from app.database.db import engine, Base

# 1. IMPORT LAHAT NG MODELS (Kailangan ito para mag-create ng tables sa Neon)
from app.models.auth_model import User
from app.models.citizen_model import ServiceRequest
from app.models.barangay_model import BarangayRecord
from app.models.municipal_model import MunicipalRecord
from app.models.provincial_model import ProvincialRecord
from app.models.routing_model import EscalationLog
from app.models.notification_model import Notification
from app.models.admin_model import AuditLog

# 2. IMPORT LAHAT NG CONTROLLERS (Base sa files mo sa screenshot)
from app.controllers import (
    auth_controller,
    citizen_controller,
    barangay_controller,
    municipal_controller,
    provincial_controller,
    routing_controller,
    notification_controller,
    admin_controller
)

# 3. CREATE TABLES SA NEON
# Ito ang nagti-trigger para lumitaw ang 8 tables sa Neon Dashboard mo
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CSR Provincial System API",
    description="Full CRUD System for Barangay, Municipal, and Provincial Levels",
    version="1.0.0"
)

# 4. REGISTER LAHAT NG ROUTERS
app.include_router(auth_controller.router)
app.include_router(citizen_controller.router)
app.include_router(barangay_controller.router)
app.include_router(municipal_controller.router)
app.include_router(provincial_controller.router)
app.include_router(routing_controller.router)
app.include_router(notification_controller.router)
app.include_router(admin_controller.router)

@app.get("/")
def root():
    return {
        "message": "CSR Backend is Online!",
        "database": "Connected to Neon",
        "entities": 8
    }