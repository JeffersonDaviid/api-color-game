from fastapi import APIRouter, Depends

from src.services.session_serv import create_session_serv, get_sessions_serv, get_sessions_patient_serv, get_session_patient_serv
from src.middlewares.verify_session import session_validator
from src.services.therapist_serv import get_therapist_serv
from src.services.patient_serv import get_patient_serv
from src.utils.error_handle import get_details_error
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response
from src.models.session_model import SessionModel

session_router = APIRouter()

@session_router.post("/register")
def post_sessions_ctrl(data: SessionModel):
    try:
        print(f"Datos recibidos en el backend: {data.dict()}")
        therapist = get_therapist_serv(cedula=data.therapist)
        if not therapist:
            return send_success_response(404, "El terapeuta no existe")
        
        patient = get_patient_serv(cedula=data.patient)
        if not patient:
            return send_success_response(404, "El paciente no existe")
        
        existing_session = get_session_patient_serv(idSesion=data.idSesion)
        if existing_session:
            return send_success_response(404, "El id de la sesión ya existe")

        session = create_session_serv(data)
        print(f"Session creado: {session.idSesion}")
        return send_success_response(201, "Session creada")
    except Exception as error:
        return get_details_error(error)
    


@session_router.get("/all")
def get_sessions_ctrl():
    try:
        sessions = get_sessions_serv()

        if not sessions:
            return send_success_response(200, "No hay sesiones registradas")

        return send_success_response(200, "Sesiones registradas", sessions)
    except Exception as error:
        return get_details_error(error)
    
@session_router.get("/{cedula}")
def get_sessions_patient_ctrl(cedula: str):
    try:
        sessions = get_sessions_patient_serv(cedula)

        if not sessions:
            return send_success_response(200, "No existen sesiones registradas para este paciente")

        return send_success_response(200, "Sesiones registradas para este paciente", sessions)
    except Exception as error:
        return get_details_error(error)