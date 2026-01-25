from fastapi import APIRouter , HTTPException
from data.kashta_data import kashtas_db

router = APIRouter()

# get all kashtas
@router.get("/kashtas")
def get_kashtas():
    # Retrieve all kashtas
    return kashtas_db

#get a single kashta
@router.get("/kashtas/{kashta_id}")
def get_single_kashta(kashta_id: int):
    # Get kashta by ID
    for kashta in kashtas_db['kashtas']:
        if kashta['id'] == kashta_id:
            return kashta
    # If tea with the given ID is not found
    raise HTTPException(status_code=404, detail="kashta not found")

# create kashta
@router.post("/kashtas")
def create_kashta(kashta: dict):
    # Create a new kashta
    kashtas_db["kashtas"].append(kashta)
    return kashta

#update kashta
@router.put("/kashtas/{kashta_id}")
def update_kashta(kashta_id: int, kashta: dict):

    # Find the kashta to update
    for existing_kashta in kashtas_db['kashtas']:
        if existing_kashta['id'] == kashta_id:
            existing_kashta.update(kashta)  # Update the existing tea's data
            return existing_kashta

    # If tea was not found, raise an error
    raise HTTPException(status_code=404, detail="kashta not found")

#delete kashta
@router.delete("/kashats/{kashta_id}")
def delete_kashta(kashta_id: int):
    # Delete a kashta by ID
    for kashta in kashtas_db['kashtas']:
        if kashta['id'] == kashta_id:
            kashtas_db['kashtas'].remove(kashta)  # Remove the kashta from the database
            return {"message": f"kashta with ID {kashta_id} has been deleted."}

    # If kashta was not found, raise an error
    raise HTTPException(status_code=404, detail="kashta not found")
