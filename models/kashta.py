from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class KashtaModel(Base):

    # This will be used directly to make a
    # TABLE in Postgresql
    __tablename__ = "kashtas"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Kashta Table.
    name = Column(String, unique=True)
    city = Column(String)
    discription = Column(String)
    price = (Integer)