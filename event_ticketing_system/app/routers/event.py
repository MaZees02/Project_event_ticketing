from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.db import get_db

router = APIRouter()

@router.post("/", response_model=schemas.EventRead)
def create_event(event_in: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db, event_in)

@router.get("/", response_model=List[schemas.EventRead])
def list_events(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.list_events(db, skip, limit)

@router.get("/{event_id}", response_model=schemas.EventRead)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = crud.get_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
