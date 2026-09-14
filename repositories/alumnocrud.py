from sqlalchemy.orm import Session
from models.alumno import Alumno

# ==================================================
# ALUMNOS (SQLAlchemy ORM)
# ==================================================

# CREATE
def crear_alumno(db: Session, nombre: str):
    nuevo_alumno = Alumno(nombre=nombre)
    db.add(nuevo_alumno)
    db.commit()
    db.refresh(nuevo_alumno)
    return nuevo_alumno

# RETRIEVE - TODOS
def obtener_alumnos(db: Session):
    return db.query(Alumno).all()

# RETRIEVE - UNO
def obtener_alumno(db: Session, alumno_id: int):
    return db.query(Alumno).filter(Alumno.id == alumno_id).first()

# UPDATE
def actualizar_alumno(db: Session, alumno_id: int, nombre: str):
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    if alumno:
        alumno.nombre = nombre
        db.commit()
        db.refresh(alumno)
    return alumno

# DELETE
def eliminar_alumno(db: Session, alumno_id: int):
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    if alumno:
        db.delete(alumno)
        db.commit()
    return alumno