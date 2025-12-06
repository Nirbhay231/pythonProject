from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

import models
import schemas


def create_user(db:Session,user:schemas.createUser):
    db_user=models.User(
        name=user.name,
        email=user.email,
        password=user.password,
        age=user.age,
        gender=user.gender
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_userdata(db:Session):
    data=db.query(models.User).all()
    return data

def get_all_users(db: Session):
    return db.query(models.User).all()


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def update_user(db: Session, id: int, updated_data: schemas.UserUpdate):
    user = get_user_by_id(db, id)
    if not user:
        return None

    if updated_data.name:
        user.name = updated_data.name
    if updated_data.email:
        user.email = updated_data.email

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, id: int):
    user = get_user_by_id(db, id)
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user
