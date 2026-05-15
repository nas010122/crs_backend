from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ang iyong Neon Connection String
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_oQVSAka6P9Rg@ep-bold-frog-ao4dxlib-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

# Gumawa ng Engine (Para sa PostgreSQL, hindi na kailangan ang check_same_thread)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal ang gagamitin natin sa Controllers para makipag-usap sa DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class para sa ating Database Models
Base = declarative_base()

# Dependency: Ito ang tinatawag sa routes para kumuha ng DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()