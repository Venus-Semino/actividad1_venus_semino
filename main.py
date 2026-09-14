from fastapi import FastAPI
from database.database import Base, engine
from routers import alumnoroutes, materiarouters 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Actividad 3")

app.include_router(alumnoroutes.router)
app.include_router(materiarouters.router)