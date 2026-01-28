from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import  relationship 
from enum import Enum
from .base import BaseModel
from .booking import BookingModel

class CategoryEnum(str, Enum):
    SUMMER = "summer"
    WINTER = "winter"

class KashtaModel(BaseModel):

    # This will be used directly to make a
    # TABLE in Postgresql
    __tablename__ = "kashtas"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Kashta Table.
    name = Column(String, unique=True)
    city = Column(String)
    discription = Column(String)
    kashtaPrice = Column(Integer)
    category = Column(SQLEnum(CategoryEnum))
    kashtaImage = Column(String, default=None)

    user_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"), nullable =False )
    #Relationship - a kshta belongs to one renter
    user = relationship('UserModel', back_populates='kashtas')

    #package
    #the relationship 1 package efers to many kashtas 
    packages = relationship('PackageModel', back_populates='kashta',  cascade="all, delete")
    #هذا التعديل عشان يقبل الحذف للكومنتات التال=بعة للتي عند الحذف 

    #booking
    # realtionship  a booking belongs to 1 kashta
    bookings = relationship('BookingModel', back_populates='kashta',  cascade="all, delete-orphan")

