from pydantic import BaseModel


class createUser(BaseModel):
    name:str
    email: str
    password: str
    age:int
    gender:str

class responseUser(createUser):
    id: int

    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    name: str | None
    email: str | None
    password: str | None
    age: int | None
    gender: str | None







