from .base import BaseModel
from sqlalchemy import Column ,Integer,String , ForeignKey ,Date
from sqlalchemy.orm import  relationship 
from .user import UserModel

class BookingModel(BaseModel):

    __tablename__ ="bookings"    #table plurl intety sigiler

    id=Column(Integer, primary_key=True , index=True)
    bookingDate = Column(Date, nullable=False)
    

    
    kashta_id = Column(Integer, ForeignKey("kashtas.id", ondelete="CASCADE"), nullable=False)
    renter_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"), nullable =False )
    # 1 booking belongs to 1 renter
    kashta = relationship("KashtaModel", back_populates="bookings", passive_deletes=True)
    renter = relationship('UserModel', back_populates='bookings', passive_deletes=True)



