from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import Base, engine, sessionLocal

app = FastAPI(
    title="EKART APPLICATION API DOCUMENTATION",
    description="""
    [Base_URL=http://127.0.0.1:8000]
    """,
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.post("/user", response_model=schemas.responseUser, status_code=201,tags=["User Profile"])
def create_user(user: schemas.createUser, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# GET ALL USERS
@app.get("/users", response_model=list[schemas.responseUser],tags=["User Profile"])
def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

# GET USER BY ID
@app.get("/users/{id}", response_model=schemas.responseUser,tags=["User Profile"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# UPDATE USER
@app.put("/users/{id}", response_model=schemas.responseUser,tags=["User Profile"])
def update_user(id: int, updated_user: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db, id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# DELETE USER
@app.delete("/users/{id}",status_code=204,tags=["User Profile"])
def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
