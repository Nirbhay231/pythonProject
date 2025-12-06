from sqlalchemy import Column, Integer, String,Boolean,DateTime
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    age= Column(Integer)
    gender = Column(String)

