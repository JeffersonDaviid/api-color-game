from fastapi import APIRouter, Depends


from src.services.patient_serv import create_patient_serv, get_patients_therapist_serv, get_patients_serv, get_patient_serv
from src.middlewares.verify_session import session_validator
from src.services.therapist_serv import get_therapist_serv
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response
from src.models.patient_model import PatientModel


patient_router = APIRouter()

@patient_router.post("/register")
def post_patients_ctrl(data: PatientModel):
    try:
        print(f"Datos recibidos en el backend: {data.dict()}")
        therapist = get_therapist_serv(cedula=data.cedulaT)
        if not therapist:
            return send_success_response(404, "El terapeuta no existe")
        
        patient = create_patient_serv(data)
        print(f"Paciente creado: {patient.name}")
        return send_success_response(201, "Paciente creado")
    except Exception as error:
        return get_details_error(error)
    
@patient_router.get("/{cedulaT}")
def get_patients_therapist_ctrl(cedulaT: str):
    try:
        patient = get_patients_therapist_serv(cedula=cedulaT)

        if not patient:
            return send_success_response(200, "No existen pacientes para este terapeuta")

        return send_success_response(200, "Pacientes encontrados para este terapeuta", patient)
    except Exception as error:
        return get_details_error(error)
    
@patient_router.get("/all")
def get_patients_ctrl():
    try:
        patients = get_patients_serv()

        if not patients:
            return send_success_response(200, "No hay pacientes registrados")

        return send_success_response(200, "Todos los pacientes registrados", patients)
    except Exception as error:
        return get_details_error(error)
    