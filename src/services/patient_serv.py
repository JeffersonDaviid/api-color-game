from src.database import Patient, Therapist
from src.models.patient_model import PatientModel
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response

def create_patient_serv(data: PatientModel):
    try:
        patient = Patient.create(
            cedulaP=data.cedulaP,
            cedulaT=data.cedulaT,
            name=data.name,
            lastname=data.lastname,
            phone=data.phone,
        )
        return patient
    except Exception as error:
        raise error;

def get_patient_serv(cedula: str):
    try:
        patient = Patient.select(
            Patient.cedulaP,
            Patient.cedulaT,
            Patient.name,
            Patient.lastname,
            Patient.phone,
        ).where(Patient.cedulaT == cedula)

        return patient.dicts().first()
    except Exception as error:
        raise error 

def get_patients_serv():
    try:
        patients = Patient.select(
            Patient.cedulaP,
            Patient.cedulaT,
            Patient.name,
            Patient.lastname,
            Patient.phone,
        )
        return list(patients.dicts())
    except Exception as error:
        raise error
    