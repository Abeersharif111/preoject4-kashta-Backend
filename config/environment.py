# config/environment.py
db_URI = "postgresql://postgres:1234@localhost:5432/kashta"
#instead of <username> write the ownwername in my db in postgres and my passwrod 1234, then replace /... with thae name of the db
import os
from dotenv import load_dotenv

load_dotenv()

db_URI = os.getenv('DATABASE_URL')
secret = os.getenv('JWT_SECRET')