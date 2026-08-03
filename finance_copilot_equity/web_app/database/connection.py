"""
Database connection module - supports SQLite (local) and PostgreSQL (Cloud SQL)
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

# Load .env variables first
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env"))
if os.path.exists(dotenv_path):
    with open(dotenv_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if v.startswith("${") and v.endswith("}"):
                    v = os.getenv(v[2:-1], "")
                if k not in os.environ:
                    os.environ[k] = v

import getpass
current_user = getpass.getuser()

# Default to local PostgreSQL database, using pg8000 driver
DATABASE_URL = os.environ.get("DATABASE_URL") or f"postgresql+pg8000://{current_user}@localhost/finance_copilot"

# Normalize connection schemes and handle pg8000 sslmode compatibility
if DATABASE_URL.startswith("postgresql://") or DATABASE_URL.startswith("postgres://"):
    prefix = "postgresql://" if DATABASE_URL.startswith("postgresql://") else "postgres://"
    DATABASE_URL = "postgresql+pg8000://" + DATABASE_URL[len(prefix):]

if "pg8000" in DATABASE_URL:
    if "?sslmode=require" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("?sslmode=require", "")
    elif "&sslmode=require" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("&sslmode=require", "")

DATABASE_PATH = None

engine = create_engine(
    DATABASE_URL,
    echo=False
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database tables"""
    from .models import Base
    Base.metadata.create_all(bind=engine)
    db_info = DATABASE_URL
    print(f"Database initialized at: {db_info}")
