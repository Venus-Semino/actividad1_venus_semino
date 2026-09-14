from sqlalchemy import Column, Integer, String
from database.database import Base # Ajusta esta importación según cómo esté definido Base en tu proyecto

class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)