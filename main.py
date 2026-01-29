# main.py

from fastapi import FastAPI
from controllers.kashtas import router as KashtasRouter  
from controllers.packages import router as PackagesRouter
from controllers.bookings import router as  BookingsRouter 
from controllers.users import router as  UsersRouter 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
     "*",
    # Later, add your deployed frontend origin, e.g.:
    # "https://your-frontend.example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Which sites can call this API
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers (e.g., Content-Type, Authorization)
)


app.include_router(KashtasRouter, prefix="/api")
app.include_router(PackagesRouter, prefix="/api")
app.include_router(BookingsRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")


@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello Kashta World!'}

