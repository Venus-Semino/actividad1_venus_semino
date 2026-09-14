from sqlalchemy.orm import Session
from models.materia import Materia

def get_materias(db: Session):
    return db.query(Materia).all()

def get_materia(db: Session, materia_id: int):
    return db.query(Materia).filter(Materia.id == materia_id).first()

def create_materia(db: Session, nombre: str):
    nueva_materia = Materia(nombre=nombre)
    db.add(nueva_materia)
    db.commit()
    db.refresh(nueva_materia)
    return nueva_materia

def update_materia(db: Session, materia_id: int, nombre: str):
    materia = db.query(Materia).filter(Materia.id == materia_id).first()
    if materia:
        materia.nombre = nombre
        db.commit()
        db.refresh(materia)
    return materia

def delete_materia(db: Session, materia_id: int):
    materia = db.query(Materia).filter(Materia.id == materia_id).first()
    if materia:
        db.delete(materia)
        db.commit()
    return materia