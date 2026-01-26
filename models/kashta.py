from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Enum as SQLEnum
from enum import Enum
from .base import BaseModel


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
    kashtaImage = Column(String)

