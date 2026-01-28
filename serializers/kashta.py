# serializers/kashta.py

from pydantic import BaseModel
from typing import Optional, List
from models.kashta import CategoryEnum
from .user import UserSchema
from .package import PackageSchema

#controling outgoing
#doing serialization when sending data to the user or browser by convert it from js to Json
class KashtaSchema(BaseModel):
  id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  city: str
  discription: str
  kashtaPrice : int
  category : CategoryEnum
  kashtaImage : Optional[str] = None

  user: UserSchema
  packages: List[PackageSchema] = []

  class Config:
    orm_mode = True
    
#controling incoming
#doing deserialization when we are getting data from the user by convert it from json to html
class CreateKashtaSchema(BaseModel):
  name: str
  city: str
  discription: str
  kashtaPrice : int 
  category : CategoryEnum
  kashtaImage : Optional[str] = None


class UpdateKashtaSchema(BaseModel):
  name: str
  city: str
  kashtaPrice : int 
  category : CategoryEnum
  kashtaImage : Optional[str] = None

