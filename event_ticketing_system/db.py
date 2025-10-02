import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# for SQLite (To check thread safety)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

def init_db():
    # This import models so they are registered with Base metadata
    import event_ticketing_system.models  
    Base.metadata.create_all(bind=engine)


# dependency for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
