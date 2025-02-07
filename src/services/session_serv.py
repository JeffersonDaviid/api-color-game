from src.database import Session, Therapist
from src.models.session_model import SessionModel
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response

def create_session_serv(data: SessionModel):
    try:
        session = Session.create(
            idSesion=data.idSesion,
            patient=data.patient,
            therapist=data.therapist,
            num_corrects=data.num_corrects,
            num_incorrects=data.num_incorrects,
            time_total=data.time_total,
            session_at=data.session_at,
        )
        return session
    except Exception as error:
        raise error

def get_sessions_patient_serv(cedula: str):
    try:
        # Obtener las sesiones del paciente
        sessions = Session.select(
            Session.idSesion,
            Session.patient,
            Session.therapist,
            Session.num_corrects,
            Session.num_incorrects,
            Session.time_total,
            Session.session_at,
        ).where(Session.patient == cedula)
        
        # Serializar las sesiones
        serialized_sessions = [
            {
                "idSesion": session.idSesion,
                "patient": session.patient.cedulaP,
                "therapist": f"{session.therapist.name} {session.therapist.lastname}",  # Obtener nombre completo del terapeuta
                "num_corrects": session.num_corrects,
                "num_incorrects": session.num_incorrects,
                "time_total": session.time_total,
                "session_at": session.session_at.isoformat(),
            }
            for session in sessions
        ]

        return serialized_sessions
    except Exception as error:
        raise error

def get_session_patient_serv(idSesion: int):
    try:
        session = Session.select(
            Session.idSesion,
            Session.patient,
            Session.therapist,
            Session.num_corrects,
            Session.num_incorrects,
            Session.time_total,
            Session.session_at,  
        ).where(Session.idSesion == idSesion).first()

        if session:
            serialized_session = {
                "idSesion": session.idSesion,
                "patient": session.patient.cedulaP,
                "therapist": session.therapist.cedulaT,
                "num_corrects": session.num_corrects,
                "num_incorrects": session.num_incorrects,
                "time_total": session.time_total,
                "session_at": session.session_at.isoformat(),

            return serialized_session
        else:
            return None
       
    except Exception as error:
        raise error


def get_sessions_serv():
    try:
        # Obtener las sesiones del paciente
        sessions = Session.select(
            Session.idSesion,
            Session.patient,
            Session.therapist,
            Session.num_corrects,
            Session.num_incorrects,
            Session.time_total,
            Session.session_at,
        ).where(Session.patient == cedula)
        
        # Serializar las sesiones
        serialized_sessions = [
            {
                "idSesion": session.idSesion,
                "patient": session.patient.cedulaP,
                "therapist": f"{session.therapist.name} {session.therapist.lastname}",  # Obtener nombre completo del terapeuta
                "num_corrects": session.num_corrects,
                "num_incorrects": session.num_incorrects,
                "time_total": session.time_total,
                "session_at": session.session_at.isoformat(),
            }
            for session in sessions
        ]

        return serialized_sessions
    except Exception as error:
        raise error
