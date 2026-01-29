from fastapi import APIRouter , Depends , HTTPException #importing the library
#SQL.ALQUMY
from sqlalchemy.orm import Session
from models.booking import BookingModel 
from models.kashta import KashtaModel
from models.user import UserModel 
#SERIALIZER
from serializers.booking import BookingSchema , CreateBookingSchema ,UpdateBookingSchema
from typing import List              
#datbase connection
from database import get_db 
from dependencies.get_current_user import get_current_user  # Import the get_current_user function



router = APIRouter()

 
#get all bookings
@router.get("/kashtas/{kashta_id}/bookings", response_model=List[BookingSchema])
def get_bookings_for_kashta(kashta_id: int, db: Session = Depends(get_db)):
    kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first()
    if not kashta:
        raise HTTPException(status_code=404, detail="kashta not found")
    return kashta.bookings

#get one booking
@router.get("/bookings/{booking_id}", response_model=BookingSchema)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="booking not found")
    return booking

#create a booking
@router.post("/kashtas/{kashta_id}/bookings", response_model=BookingSchema)
def create_booking(kashta_id: int, booking: CreateBookingSchema, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first()
    if not kashta:
        raise HTTPException(status_code=404, detail="kashta not found")
    
    new_booking = BookingModel(**booking.dict(), kashta_id=kashta_id , renter_id=current_user.id)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

#update the booking
@router.put("/bookings/{booking_id}", response_model=BookingSchema)
def update_booking(booking_id: int, booking: UpdateBookingSchema, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="booking not found")
    
    # Check if the current user is the creator of the tea
    if db_booking.user_id != current_user.id:
       raise HTTPException(status_code=403, detail="Operation forbidden")
    
    booking_form_data = booking.dict(exclude_unset=True) 
    for key, value in booking_form_data.items():   
             setattr(db_booking, key, value)  
             db.commit()  
             db.refresh(db_booking) 
             return db_booking

@router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    db_booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="booking not found")
    # Check if the current user is the creator of the tea
    if db_booking.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    db.delete(db_booking)
    db.commit()
    return {"message": f"Booking with ID {booking_id} has been deleted"}