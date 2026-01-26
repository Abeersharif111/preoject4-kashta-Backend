#controllers/kashtas.py
from fastapi import APIRouter , Depends , HTTPException #importing the library
#SQL.ALQUMY
from sqlalchemy.orm import Session
from models.kashta import KashtaModel
from models.user import UserModel
#SERIALIZER
from serializers.kashta import KashtaSchema , CreateKashtaSchema ,UpdateKashtaSchema
from typing import List              
#datbase connection
from database import get_db 
#middleware
from dependencies.get_current_user import get_current_user  # Import the get_current_user function

router = APIRouter()

#Create an index route to GET all /kashtas/
@router.get("/kashtas",response_model= List[KashtaSchema]) # it can be ('/') also , this is when we send out to the user that was it ie response which is ((((serialization))))
#list means to view all the list of tea becouse it is the index page
def get_kashtas(db : Session = Depends(get_db)): #means is it a valid session of the db (get_db() connecting the db) depends givs it the awit
                # this is the req,res ..
    # Retrieve all teas
    kashtas = db.query(KashtaModel).all()
    #database model query from teamodle bring all 
    return kashtas

#Read/GET Single Tea Route
@router.get("/kashtas/{kashta_id}", response_model=KashtaSchema)
def get_single_kashta(kashta_id: int, db: Session = Depends(get_db)):
    kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first()
    if not kashta:                                           # first to take the first result of the filter or it my take an empty
        raise HTTPException(status_code=404, detail="kashta not found")
    return kashta



#create/POST Route
@router.post("/kashtas", response_model=KashtaSchema)
def create_kashta(kashta: CreateKashtaSchema, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    new_kashta = KashtaModel(**kashta.dict(),user_id=current_user.id) # Convert Pydantic model to SQLAlchemy model # ** is the keyes same of (...props)
    db.add(new_kashta)   #add it to th db
    db.commit() # Save to database
    db.refresh(new_kashta) # Refresh to get the updated data (including auto-generated fields)

    return new_kashta

#update 
@router.put("/kashtas/{kashta_id}", response_model=KashtaSchema)
def update_kashta(kashta_id: int , kashta : UpdateKashtaSchema, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    db_kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first()
    if not db_kashta:
        raise HTTPException(status_code=404, detail="kashta not found")

# Check if the current user is the creator of the kashta
    if db_kashta.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    kashta_data = kashta.dict(exclude_unset=True)  # Only update the fields provided , then we are converting the class to dictionary and then loop through it (dict= dictionary)
    for key, value in kashta_data.items():
        setattr(db_kashta, key, value) # giving the key and value values to the db_tea 

    db.commit()  # Save changes
    db.refresh(db_kashta)  # Refresh to get updated data updating the timestamp
    return db_kashta


@router.delete("/kashtas/{kashta_id}") # we didnt use the serializer bcuse there is no=i recrds to be reterned in delete thats why no need to (response_model=TeaSchema)
def delete_kashta(kashta_id: int, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    db_kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first() #finding the wanted record
    if not db_kashta:
        raise HTTPException(status_code=404, detail="kashta not found")

# Check if the current user is the creator of the tea
    if db_kashta.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    db.delete(db_kashta)  # Remove from database
    db.commit()  # Save changes
    return {"message": f"kashta with ID {kashta_id} has been deleted"}

