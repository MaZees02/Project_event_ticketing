from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# --- User ---
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# --- Event ---
class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = 0.0
    capacity: Optional[int] = 0

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- Ticket ---
class TicketCreate(BaseModel):
    event_id: int
    owner_id: int

class TicketRead(BaseModel):
    id: int
    event_id: int
    owner_id: int
    qr_code: Optional[str] = None
    is_used: bool
    purchased_at: datetime

    class Config:
        orm_mode = True

# --- Payment ---
class PaymentCreate(BaseModel):
    user_id: Optional[int]
    event_id: Optional[int]
    amount: float
    provider: Optional[str] = "paystack"

class PaymentRead(BaseModel):
    id: int
    user_id: Optional[int]
    event_id: Optional[int]
    amount: float
    provider: Optional[str]
    status: str
    reference: Optional[str]

    class Config:
        orm_mode = True
