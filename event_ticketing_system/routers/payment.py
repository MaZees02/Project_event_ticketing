from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from event_ticketing_system import schemas
from event_ticketing_system.db import get_db
from event_ticketing_system import crud

router = APIRouter()

@router.post("/", response_model=schemas.PaymentRead)
def create_payment(payment_in: schemas.PaymentCreate, db: Session = Depends(get_db)):
    
    p = crud.create_payment(db, payment_in)
    return p

@router.get("/", response_model=List[schemas.PaymentRead])
def list_payments(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.list_payments(db, skip, limit)

@router.get("/{payment_id}", response_model=schemas.PaymentRead)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    p = crud.get_payment(db, payment_id)
    if not p:
        raise HTTPException(status_code=404, detail="Payment not found")
    return p
