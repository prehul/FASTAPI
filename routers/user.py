from fastapi import Response, Depends, status, HTTPException, FastAPI
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/')
def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    # db.refresh(new_user)
    return new_user

@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with the id {id} is not available")
    return user