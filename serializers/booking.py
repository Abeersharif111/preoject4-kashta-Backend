# serializers/booking.py

from pydantic import BaseModel
from typing import Optional
from models.user import UserModel
from .user import UserSchema
from datetime import date



class BookingSchema(BaseModel):
  id: int
  bookingDate : date
  renter: UserSchema

  class Config:
    orm_mode = True
    
 #creatpackageschema   
class CreateBookingSchema(BaseModel):
   bookingDate : date

#updatecommentschema
class UpdateBookingSchema(BaseModel):
    bookingDate : date