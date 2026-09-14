from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db # Ajusta si tu función de conexión se llama distinto
from repositories import materiacrud

router = APIRouter(prefix="/materias", tags=["materias"])

@router.post("/")
def crear_materia(nombre: str, db: Session = Depends(get_db)):
    return materiacrud.create_materia(db, nombre)

@router.get("/")
def leer_materias(db: Session = Depends(get_db)):
    return materiacrud.get_materias(db)

@router.get("/{materia_id}")
def leer_materia(materia_id: int, db: Session = Depends(get_db)):
    materia = materiacrud.get_materia(db, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia

@router.put("/{materia_id}")
def actualizar_materia(materia_id: int, nombre: str, db: Session = Depends(get_db)):
    materia = materiacrud.update_materia(db, materia_id, nombre)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia

@router.delete("/{materia_id}")
def eliminar_materia(materia_id: int, db: Session = Depends(get_db)):
    materia = materiacrud.delete_materia(db, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return {"mensaje": "Materia eliminada exitosamente"}