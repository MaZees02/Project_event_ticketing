from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from event_ticketing_system.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tickets = relationship("Ticket", back_populates="owner")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    location = Column(String(255))
    date = Column(String(50))
    price = Column(Float, default=0.0)
    capacity = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    tickets = relationship("Ticket", back_populates="event")

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    qr_code = Column(String(512), nullable=True)  # store QR payload or path
    purchased_at = Column(DateTime, default=datetime.utcnow)
    is_used = Column(Boolean, default=False)

    event = relationship("Event", back_populates="tickets")
    owner = relationship("User", back_populates="tickets")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    amount = Column(Float, nullable=False)
    provider = Column(String(100), nullable=True)  # 'paystack', 'stripe', etc.
    status = Column(String(50), default="pending")  # pending, success, failed
    created_at = Column(DateTime, default=datetime.utcnow)
    reference = Column(String(255), unique=True, index=True, nullable=True)
