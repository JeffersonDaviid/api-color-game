from fastapi import APIRouter, Depends

from src.middlewares.verify_session import session_validator
from src.services.therapist_serv import get_therapist_serv, get_therapists_serv
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response

therapist_router = APIRouter()


@therapist_router.get("/all", dependencies=[Depends(session_validator)])
def get_therapists_ctrl():
    try:
        therapists = get_therapists_serv()

        if not therapists:
            return send_success_response(200, "No hay usuarios registrados")

        return send_success_response(200, "Usuarios registrados", therapists)
    except Exception as error:
        return get_details_error(error)


@therapist_router.get("/{cedula}", dependencies=[Depends(session_validator)])
def get_therapist_ctrl(cedula: str):
    try:
        therapist = get_therapist_serv(cedula=cedula)

        if not therapist:
            return send_success_response(200, "El usuario no existe")

        return send_success_response(200, "Usuario encontrado", therapist)
    except Exception as error:
        return get_details_error(error)
