from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    last_name: str
    email:str
    phone: str

class ModelSchema(BaseModel):
    movie_name: str
    release_year: int
    duration: int
    director: str
    clasification: str
    genre: str

