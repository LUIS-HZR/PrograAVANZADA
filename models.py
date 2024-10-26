from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
    __tablename__= "movies"

    id: int = Field(primary_key=True)

    movie_name: str
    release_year: int
    duration: int
    director: str
    clasification: str
    genre: str
    