#here we will do same as set in json to remove th epassword from the token
from pydantic import BaseModel

#هنا نعرف الكلاس الخاص بالمعلومات الداخلة من الخارجة عنان اللي فيها باسورد بتكون الداخله و اللي فيها كونفج هي الداخلة عشان نعرفها بالكونفجريشن اللي موجود عندنا في الداتابيس
class UserRegistrationSchema(BaseModel):
    username: str  # User's unique name
    password: str  # Plain text password for user registration (will be hashed before saving)

# login schema
# New schema for user login (captures username and password during login)
class UserLoginSchema(BaseModel):
    username: str  # Username provided by the user during login
    password: str  # Plain text password provided by the user during login
    # user_role: str
    
# New schema for the response (containing the JWT token and a success message)
class UserTokenSchema(BaseModel):
    token: str  # JWT token generated upon successful login
    message: str  # Success message like welcomeback msg

    class Config:
        orm_mode = True


# Schema for returning user data (without exposing the password)
class UserSchema(BaseModel):  # convering body to json from th edatabese to outside and also becuse id dont have the password
    username: str
    user_role: str

    class Config:
        orm_mode = True 
