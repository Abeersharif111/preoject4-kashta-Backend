from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel  #these are the 2 differnt between the conrollers
from serializers.user import UserSchema, UserRegistrationSchema ,UserLoginSchema,UserTokenSchema  #these are the 2 differnt between the conrollers
from database import get_db

router = APIRouter()

@router.post("/register", response_model=UserSchema)
def create_user(user: UserRegistrationSchema, db: Session = Depends(get_db)):
    #1- Check if the username or email already exists and uniqe
    existing_user = db.query(UserModel).filter(UserModel.username == user.username ).first()  #here checking one of them is wrong
                                #this is python or
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = UserModel(username=user.username, role=user.role) #2-put the user in memory then
    # Use the set_password method to hash the password
    new_user.set_password(user.password) #3- call the metod to crypt the password

    db.add(new_user) 
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=UserTokenSchema)
def login(user: UserLoginSchema, db: Session = Depends(get_db)):

    # Find the user by username
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()

    # Check if the user exists and if the password is correct
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    token = db_user.generate_token()
           #this is the instance in the db
    # Return token and a success message
    return {"token": token, "message": "Login successful"}


