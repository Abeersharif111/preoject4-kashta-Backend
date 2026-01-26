from .base import BaseModel
from sqlalchemy import Column ,Integer,String , ForeignKey 
from sqlalchemy.orm import  relationship 
#from .user import UserModel

class PackagetModel(BaseModel):

    __tablename__ ="packages"    #table plurl intety sigiler

    id=Column(Integer, primary_key=True , index=True)
    name = Column(String, nullable=False)
    discription = Column(String,nullable=False)
    packageprice = Column(Integer,nullable=False)
    packageImage = Column( String ,nullable=False)

    # CommentModel
    kashta_id = Column(Integer, ForeignKey("kashtas.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"), nullable =False )
    
    kashta = relationship("KashtaModel", back_populates="packages", passive_deletes=True)
    user = relationship('UserModel', back_populates='packages', passive_deletes=True)



