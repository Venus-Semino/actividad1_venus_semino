from pydantic import BaseModel


class AlumnoCreate(BaseModel):
    nombre: str


class AlumnoUpdate(BaseModel):
    nombre: str