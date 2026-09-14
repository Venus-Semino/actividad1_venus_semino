from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Se deja únicamente la importación correcta de los esquemas
from models.alumno import AlumnoCreate, AlumnoUpdate 
from database.database import get_db

from repositories.alumnocrud import (
    crear_alumno,
    obtener_alumnos,
    obtener_alumno,
    actualizar_alumno,
    eliminar_alumno,
)

router = APIRouter()

# ==================================================
# HOLA MUNDO
# ==================================================
@router.get("/")
def hola_mundo():
    return {
        "mensaje": "Hola Mundo"
    }

# ==================================================
# SALUDO
# ==================================================
@router.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {
        "nombre": nombre,
        "mensaje": f"Hola {nombre}, bienvenido a FastAPI"
    }

# ==================================================
# CRUD ALUMNOS
# ==================================================

# CREATE
@router.post("/alumnos")
def agregar_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db)):
    nuevo_alumno = crear_alumno(db, alumno.nombre)
    return {
        "mensaje": "Alumno creado correctamente",
        "alumno": nuevo_alumno
    }

# RETRIEVE - TODOS
@router.get("/alumnos")
def listar_alumnos(db: Session = Depends(get_db)):
    return obtener_alumnos(db)

# RETRIEVE - UNO
@router.get("/alumnos/{alumno_id}")
def consultar_alumno(alumno_id: int, db: Session = Depends(get_db)):
    alumno = obtener_alumno(db, alumno_id)
    if alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

# UPDATE
@router.put("/alumnos/{alumno_id}")
def modificar_alumno(alumno_id: int, alumno: AlumnoUpdate, db: Session = Depends(get_db)):
    alumno_actualizado = actualizar_alumno(db, alumno_id, alumno.nombre)
    if alumno_actualizado is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {
        "mensaje": "Alumno actualizado correctamente",
        "alumno": alumno_actualizado
    }

# DELETE
@router.delete("/alumnos/{alumno_id}")
def borrar_alumno(alumno_id: int, db: Session = Depends(get_db)):
    alumno_eliminado = eliminar_alumno(db, alumno_id)
    if alumno_eliminado is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {
        "mensaje": "Alumno eliminado correctamente",
        "alumno": alumno_eliminado
    }