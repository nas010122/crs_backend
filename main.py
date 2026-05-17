from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware  # <-- 1. Idinagdag na Import para sa Front-end
from app.database.db import engine, Base
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

# 1. IMPORT MODELS
from app.models.auth_model import User
from app.models.citizen_model import ServiceRequest
from app.models.barangay_model import BarangayRecord
from app.models.municipal_model import MunicipalRecord
from app.models.provincial_model import ProvincialRecord
from app.models.routing_model import EscalationLog
from app.models.notification_model import Notification
from app.models.admin_model import AuditLog

# 2. IMPORT CONTROLLERS
from app.controllers import (
    auth_controller, citizen_controller, barangay_controller,
    municipal_controller, provincial_controller, routing_controller,
    notification_controller, admin_controller
)

# 3. CREATE TABLES
Base.metadata.create_all(bind=engine)

# 4. SECURITY CONFIG (Ito ang "Susi" para lumabas ang Lock Icon)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# 5. INITIALIZE APP WITH SECURITY SCHEME
app = FastAPI(
    title="CSR Provincial System API",
    description="Full CRUD System for Tawi-Tawi Management",
    version="1.0.0",
    swagger_ui_parameters={"deepLinking": True}
)

# --- 2. DITO ISININGIT ANG CORS MIDDLEWARE CONFIGURATION ---
# Pinapayagan natin ang front-end na kumonekta kahit magkaiba kayo ng port o kahit galing sa phone emulator
origins = [
    "http://localhost:3000",      # Kung React/Vue/Next.js ang gamit sa web
    "http://localhost:8080",      # Iba pang web servers
    "http://127.0.0.1:3000",
    "*",                          # Ang "*" ay "Allow All" - Napaka-importante para sa Flutter Mobile Apps!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],          # Pinapayagan ang GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],          # Pinapayagan ang Authorization headers at Tokens
)
# ----------------------------------------------------------

# 6. REGISTER ROUTERS
app.include_router(auth_controller.router, prefix="/auth", tags=["Authentication"])
app.include_router(citizen_controller.router, prefix="/citizen", tags=["Citizen Services"])
app.include_router(barangay_controller.router, prefix="/barangay", tags=["Barangay Level"])
app.include_router(municipal_controller.router, prefix="/municipal", tags=["Municipal Level"])
app.include_router(provincial_controller.router, prefix="/provincial", tags=["Provincial Level"])
app.include_router(routing_controller.router, prefix="/routing", tags=["Routing & Escalation"])
app.include_router(notification_controller.router, prefix="/notifications", tags=["Notifications"])
app.include_router(admin_controller.router, prefix="/admin", tags=["Admin & Audit"])

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "CSR Backend is Online!",
        "database": "Connected to Neon",
        "owner": "Aljan Andy"
    }

# Halimbawa ng protektadong route para lumitaw ang lock sa documentation
@app.get("/check-lock", tags=["Security Test"])
def test_lock(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"status": "Lock icon is active!", "token": token}