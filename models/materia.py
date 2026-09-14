from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database.database import Base

# Modelo ORM (SQLAlchemy)
class Materia(Base):
    __tablename__ = "materias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

# Esquemas Pydantic para los body de FastAPI
class MateriaCreate(BaseModel):
    nombre: str

class MateriaUpdate(BaseModel):
    nombre: str