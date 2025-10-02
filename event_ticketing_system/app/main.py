# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import init_db, engine
from app.routers import user, event, ticket, payment

app = FastAPI(title="Merged Event Ticketing API")

# CORS (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(event.router, prefix="/events", tags=["events"])
app.include_router(ticket.router, prefix="/tickets", tags=["tickets"])
app.include_router(payment.router, prefix="/payments", tags=["payments"])


@app.on_event("startup")
def on_startup():
    # Create tables if they don't exist
    init_db()


@app.get("/")
def root():
    return {"status": "ok", "service": "Merged Event Ticketing API"}
