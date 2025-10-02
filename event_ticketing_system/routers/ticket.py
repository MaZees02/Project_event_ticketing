from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from event_ticketing_system import schemas
from event_ticketing_system.db import get_db
from event_ticketing_system import crud

router = APIRouter()

@router.post("/", response_model=schemas.TicketRead)
def purchase_ticket(ticket_in: schemas.TicketCreate, db: Session = Depends(get_db)):
    # Basic validation
    event = crud.get_event(db, ticket_in.event_id)
    user = crud.get_user(db, ticket_in.owner_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    ticket = crud.create_ticket(db, ticket_in)
    return ticket

@router.get("/{ticket_id}", response_model=schemas.TicketRead)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    t = crud.get_ticket(db, ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return t

@router.get("/event/{event_id}", response_model=List[schemas.TicketRead])
def list_tickets_event(event_id: int, db: Session = Depends(get_db)):
    return crud.list_tickets_for_event(db, event_id)
