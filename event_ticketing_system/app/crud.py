from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
import uuid

import app.models as models
import app.schemas as schemas

# Users
def create_user(db: Session, user_in: schemas.UserCreate) -> models.User:
    user = models.User(email=user_in.email, full_name=user_in.full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.get(models.User, user_id)

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.scalar(select(models.User).where(models.User.email==email))

def list_users(db: Session, skip: int=0, limit: int=100) -> List[models.User]:
    return db.scalars(select(models.User).offset(skip).limit(limit)).all()

# Events
def create_event(db: Session, event_in: schemas.EventCreate) -> models.Event:
    ev = models.Event(**event_in.dict())
    db.add(ev)
    db.commit()
    db.refresh(ev)
    return ev

def get_event(db: Session, event_id: int) -> Optional[models.Event]:
    return db.get(models.Event, event_id)

def list_events(db: Session, skip: int=0, limit: int=100) -> List[models.Event]:
    return db.scalars(select(models.Event).offset(skip).limit(limit)).all()

# Tickets
def create_ticket(db: Session, ticket_in: schemas.TicketCreate) -> models.Ticket:
    # simple QR payload generation (UUID)
    qr = str(uuid.uuid4())
    ticket = models.Ticket(event_id=ticket_in.event_id, owner_id=ticket_in.owner_id, qr_code=qr)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_ticket(db: Session, ticket_id: int) -> Optional[models.Ticket]:
    return db.get(models.Ticket, ticket_id)

def list_tickets_for_event(db: Session, event_id: int):
    return db.scalars(select(models.Ticket).where(models.Ticket.event_id==event_id)).all()

# Payments (very simplified)
def create_payment(db: Session, payment_in: schemas.PaymentCreate) -> models.Payment:
    reference = str(uuid.uuid4())
    p = models.Payment(
        user_id=payment_in.user_id,
        event_id=payment_in.event_id,
        amount=payment_in.amount,
        provider=payment_in.provider,
        status="pending",
        reference=reference
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def get_payment(db: Session, payment_id: int):
    return db.get(models.Payment, payment_id)

def list_payments(db: Session, skip: int=0, limit: int=100):
    return db.scalars(select(models.Payment).offset(skip).limit(limit)).all()
