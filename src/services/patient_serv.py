from src.database import Patient, Therapist
from src.models.patient_model import PatientModel
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response

def create_patient_serv(data: PatientModel):
    try:
        # Valida si ya existe un paciente con la misma cédula
        existing_patient = Patient.get_or_none(Patient.cedulaP == data.cedulaP)
        if existing_patient:
            raise ValueError("El paciente ya existe con la misma cédula")
        
        patient = Patient.create(
            cedulaP=data.cedulaP,
            name=data.name,
            lastname=data.lastname,
            phone=data.phone,
            cedulaT=data.cedulaT,
        )
        return patient
    except Exception as error:
        raise error;

def get_patient_serv(cedula: str):
    try:
        patients = Patient.select(
            Patient.cedulaP,
            Patient.name,
            Patient.lastname,
            Patient.phone,
            Patient.cedulaT,
        ).where(Patient.cedulaT == cedula)

        return list(patients.dicts())
    except Exception as error:
        raise error 

def get_patients_serv():
    try:
        patients = Patient.select(
            Patient.cedulaP,
            Patient.name,
            Patient.lastname,
            Patient.phone,
            Patient.cedulaT,
        )
        return list(patients.dicts())
    except Exception as error:
        raise error
    