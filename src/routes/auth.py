from datetime import timedelta

from fastapi import APIRouter

from src.models.auth_model import AuthModel
from src.models.therapist_model import TherapistModel
from src.services.auth_serv import get_auth_therapist_serv
from src.services.therapist_serv import create_therapist_serv
from src.utils.bcrypt_handle import verified
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response
from src.utils.jwt_handle import generate_token

auth_router = APIRouter()


@auth_router.post("/login")
def post_therapists_ctrl(data: AuthModel):
    try:
        therapist = get_auth_therapist_serv(data.cedulaT)

        if not therapist:
            return send_success_response(404, "Usuario no encontrado")

        if not verified(data.password, therapist["password"]):
            return send_success_response(401, "Contraseña incorrecta")

        token = generate_token(therapist, expires_in=timedelta(minutes=1))

        return send_success_response(201, "Usuario login", {"token": token})
    except Exception as error:
        return get_details_error(error)


@auth_router.post("/register")
def post_therapists_ctrl(data: TherapistModel):
    try:
        therapist = create_therapist_serv(data)
        print(f"Usuario creado: {therapist.name}")
        return send_success_response(
            201, "Usuario creado", therapist["cedulaT", "name", "lastName"]
        )
    except Exception as error:
        return get_details_error(error)


@auth_router.get("/logout")
def get_therapists_ctrl():
    return send_success_response(200, "Usuario deslogueado")
