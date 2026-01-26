from fastapi import APIRouter , Depends , HTTPException #importing the library
#SQL.ALQUMY
from sqlalchemy.orm import Session
from models.package import PackagetModel 
from models.kashta import KashtaModel
from models.user import UserModel 
#SERIALIZER
from serializers.package import PackageSchema , CreatePackageSchema ,UpdatePackageSchema
from typing import List              
#datbase connection
from database import get_db 
from dependencies.get_current_user import get_current_user  # Import the get_current_user function



router = APIRouter()

 
#get all packages
@router.get("/kashtas/{kashta_id}/packages", response_model=List[PackageSchema])
def get_packages_for_kashta(kashta_id: int, db: Session = Depends(get_db)):
    kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first()
    if not kashta:
        raise HTTPException(status_code=404, detail="kashta not found")
    return kashta.packages

#get one package
@router.get("/packages/{package_id}", response_model=PackageSchema)
def get_package(package_id: int, db: Session = Depends(get_db)):
    package = db.query(PackagetModel).filter(PackagetModel.id == package_id).first()
    if not package:
        raise HTTPException(status_code=404, detail="Comment not found")
    return package

#create a package
@router.post("/kashtas/{kashta_id}/packages", response_model=PackageSchema)
def create_package(kashta_id: int, package: CreatePackageSchema, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    kashta = db.query(KashtaModel).filter(KashtaModel.id == kashta_id).first()
    if not kashta:
        raise HTTPException(status_code=404, detail="kashta not found")
    
    new_package = PackagetModel(**package.dict(), kashta_id=kashta_id , user_id=current_user.id)
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return new_package

#update the package
@router.put("/packages/{package_id}", response_model=PackageSchema)
def update_package(package_id: int, package: UpdatePackageSchema, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    db_package = db.query(PackagetModel).filter(PackagetModel.id == package_id).first()
    if not db_package:
        raise HTTPException(status_code=404, detail="package not found")
    
    # Check if the current user is the creator of the tea
    if db_package.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    package_data = package.dict(exclude_unset=True)
    for key, value in package_data.items():
        setattr(db_package, key, value)
    db.commit()
    db.refresh(db_package)
    return  db_package

@router.delete("/packages/{package_id}")
def delete_package(package_id: int, db: Session = Depends(get_db),current_user: UserModel = Depends(get_current_user)):
    db_package = db.query(PackagetModel).filter(PackagetModel.id == package_id).first()
    if not db_package:
        raise HTTPException(status_code=404, detail="package not found")
    # Check if the current user is the creator of the tea
    if db_package.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    db.delete(db_package)
    db.commit()
    return {"message": f"Package with ID {package_id} has been deleted"}