from fastapi import FastAPI

app = FastAPI()

# Endpoint raiz (para ver si funciona)
@app.get("/")
def root():
    return {"mensaje": "La aplicación Backend se encuentra funcionando."}

#  Información ALUMNO

@app.get("/alumno")
def obtener_alumno():
    return {
        "nombre": "Venus Getsemaní Semino Alemán",
        "semestre": "4to. cuatrimestre",
        "carrera": "TSU en Desarrollo e Innovación de Software",
        "año ingresado": "2025"
    }

# Endpoint con la lista de materias
@app.get("/materias")
def obtener_materias():
    return [
        {
            "id": 1,
            "nombre": "Programación"
        },
        {
            "id": 2,
            "nombre": "Base de Datos"
        },
        {
            "id": 3,
            "nombre": "Desarrollo Backend"
        }
    ]

# Endpoint MATERIA url ruta
@app.get("/materias/{materia_id}")
def obtener_materia(materia_id: int):
    return {
        "id": materia_id,
        "mensaje": f"Consultando la materia {materia_id}"
    }

# Reto SALUDOOOO
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {
        "mensaje": f"Hola {nombre}, bienvenido a FastAPI"
    }


# NOTA: para la actividad 2 separar en capas, en las carpetas