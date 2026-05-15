from fastapi import FastAPI, Depends
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
# Ang 'tokenUrl' ay dapat tumuturo sa exact path ng login function mo mamaya
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# 5. INITIALIZE APP WITH SECURITY SCHEME
app = FastAPI(
    title="CSR Provincial System API",
    description="Full CRUD System for Tawi-Tawi Management",
    version="1.0.0",
    # Dito natin idedeklara ang security requirements globally
    swagger_ui_parameters={"deepLinking": True}
)

# 6. REGISTER ROUTERS (Inalis ko ang redundant /auth sa prefix)
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