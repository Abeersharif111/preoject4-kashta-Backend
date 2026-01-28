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
  packageImage : Optional[str] = None
  owner: UserSchema

  
  class Config:
    orm_mode = True
    
 #creatpackageschema   
class CreatePackageSchema(BaseModel):
  name :str
  discription : str
  packageprice : int
  packageImage : Optional[str] = None


#updatecommentschema
class UpdatePackageSchema(BaseModel):
   name :str
   discription : str
   packageprice : int
   packageImage : Optional[str] = None