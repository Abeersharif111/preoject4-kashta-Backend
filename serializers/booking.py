# serializers/booking.py

from pydantic import BaseModel
from typing import Optional
from models.user import UserModel
from .user import UserSchema
from datetime import date



class BookingSchema(BaseModel):
  id: int
  bookingDate : date
  
  user: UserSchema

  
  class Config:
    orm_mode = True
    
 #creatpackageschema   
class CreateBookingSchema(BaseModel):
   bookingDate : date



   class Config:
    orm_mode = True #means using sqlalqumy

#updatecommentschema
class UpdateBookingSchema(BaseModel):
    bookingDate : date


    class Config:
     orm_mode = True