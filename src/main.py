from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from src.routes.auth import auth_router
from src.routes.therapist import therapist_router
from src.utils.handle_respose import send_error_response

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Bienvenido a Memoria Artística</h1>"


app.include_router(therapist_router, prefix="/api/v1/therapist")
app.include_router(auth_router, prefix="/api/v1/auth")


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc: HTTPException):
    # Comprobamos si `exc.detail` es un dict, y lo formateamos.
    if isinstance(exc.detail, dict):
        return send_error_response(
            exc.status_code, exc.detail["message"], exc.detail["error"]
        )
    return send_error_response(exc.status_code, exc.detail)
