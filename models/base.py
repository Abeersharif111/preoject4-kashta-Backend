from sqlalchemy import Column, Integer,DateTime , func # column is a property
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):#base inherting from declarative-base

    
    __abstract__=True # it is virtual which means only to inheret

    id = Column(Integer, primary_key=True, index=True)

    created_at= Column (DateTime,default=func.now())# Timestamp for when the record was created
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Auto-updates on changes 

    