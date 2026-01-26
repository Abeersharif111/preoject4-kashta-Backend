# serializers/package.py

from pydantic import BaseModel
from typing import Optional
from models.user import UserModel
from .user import UserSchema


class PackageSchema(BaseModel):
  id: int
  name :str
  discription : str
  packageprice : int
  packageImage : str

  user: UserSchema

  
  class Config:
    orm_mode = True
    
 #creatpackageschema   
class CreatePackageSchema(BaseModel):
  name :str
  discription : str
  packageprice : int
  packageImage : str



  class Config:
    orm_mode = True #means using sqlalqumy

#updatecommentschema
class UpdatePackageSchema(BaseModel):
   name :str
   discription : str
   packageprice : int
   packageImage : str


   class Config:
    orm_mode = True