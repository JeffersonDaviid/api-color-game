from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.routes import therapist

therapists = []

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Bienvenido a Memoria Artística</h1>"


app.include_router(therapist.therapist_router)
