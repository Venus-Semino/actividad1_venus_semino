from fastapi import FastAPI

from routers.routes import router


app = FastAPI(
    title="API de Alumnos",
    version="1.0.0"
)


# ==================================================
# ROUTES
# ==================================================

app.include_router(router)