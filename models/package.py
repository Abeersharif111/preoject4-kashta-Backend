from .base import BaseModel
from sqlalchemy import Column ,Integer,String , ForeignKey 
from sqlalchemy.orm import  relationship 
from .user import UserModel

class PackageModel(BaseModel):

    __tablename__ ="packages"    #table plurl intety sigiler

    id=Column(Integer, primary_key=True , index=True)
    name = Column(String, nullable=False)
    discription = Column(String,nullable=False)
    packageprice = Column(Integer,nullable=False)
    packageImage = Column( String, default=None)

    # 
    kashta_id = Column(Integer, ForeignKey("kashtas.id", ondelete="CASCADE"), nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"))
    # 1 kashta belongs to 1 renter
    kashta = relationship("KashtaModel", back_populates='packages')
    owner = relationship('UserModel', back_populates='packages', passive_deletes=True)



