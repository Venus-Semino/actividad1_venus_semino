from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db # Importación corregida
from repositories import materiacrud
from models.materia import MateriaCreate, MateriaUpdate # Importa los nuevos esquemas

router = APIRouter(prefix="/materias", tags=["materias"])

# Actualiza tus endpoints para usar los esquemas en lugar del string suelto:
@router.post("/")
def crear_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    return materiacrud.create_materia(db, materia.nombre)

@router.put("/{materia_id}")
def actualizar_materia(materia_id: int, materia: MateriaUpdate, db: Session = Depends(get_db)):
    return materiacrud.update_materia(db, materia_id, materia.nombre)


@router.get("/")
def leer_materias(db: Session = Depends(get_db)):
    return materiacrud.get_materias(db)

@router.get("/{materia_id}")
def leer_materia(materia_id: int, db: Session = Depends(get_db)):
    materia = materiacrud.get_materia(db, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia

@router.delete("/{materia_id}")
def eliminar_materia(materia_id: int, db: Session = Depends(get_db)):
    materia = materiacrud.delete_materia(db, materia_id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return {"mensaje": "Materia eliminada exitosamente"}