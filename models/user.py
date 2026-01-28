# models/user.py

from sqlalchemy import Column, Integer, String
from .base import BaseModel
from passlib.context import CryptContext # Import new package
import jwt  # New import for token generation
from datetime import datetime, timedelta , timezone # New import for timestamps
from sqlalchemy.orm import relationship # add relationship

# Import the secret from the environment file
from config.environment import secret

# Creating a password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # use teh dcrypt and double check if it is secure

class UserModel(BaseModel):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False,unique=True)  # Each username must be unique
    password = Column(String, nullable=True , unique=True)  # Add new field for storing the hashed password
    user_role = Column(String, nullable=False, default="customer")  # Each email must be unique

#relationships
    # NEW: Relationship - a user can have multiple kashtas , packages , bookings
  
    kashtas = relationship('KashtaModel', back_populates='user',cascade="all,delete-orphan")
    packages = relationship('PackageModel', back_populates='owner',  cascade="all, delete-orphan")
    bookings = relationship("BookingModel", back_populates="renter",cascade="all, delete-orphan")

     


# Method to hash and store the password
    def set_password(self, password: str):    #self here means instatnt method
        self.password = pwd_context.hash(password)

  # Method to verify the password
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)
    
  # Method to generate a JWT token
    def generate_token(self):
        # Define the payload
        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),  # Expiration time (1 day)
            "iat": datetime.now(timezone.utc),  # Issued at time
            "sub": str(self.id),  # Subject - the user ID need to be converted to string instaed of int bcs puthon not accept it
            "username": self.username,
            "user_role": self.user_role
        }

        # Create the JWT token
        token = jwt.encode(payload, secret, algorithm="HS256")

        return token   
    
