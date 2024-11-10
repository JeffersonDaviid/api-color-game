from src.database import Therapist
from src.models.therapist_model import TherapistModel
from src.utils.bcrypt_handle import encrypt


def get_therapists_serv():
    try:
        therapists = Therapist.select(
            Therapist.cedulaT,
            Therapist.name,
            Therapist.lastname,
            Therapist.email,
            Therapist.phone,
        )
        return list(therapists.dicts())
    except Exception as error:
        raise error


def get_therapist_serv(cedula: str):
    try:
        therapist = Therapist.select(
            Therapist.cedulaT,
            Therapist.name,
            Therapist.lastname,
            Therapist.email,
            Therapist.phone,
        ).where(Therapist.cedulaT == cedula)

        return therapist.dicts().first()
    except Exception as error:
        raise error


def create_therapist_serv(data: TherapistModel):
    try:
        passwordHashed = encrypt(data.password)

        user = Therapist.create(
            cedulaT=data.cedulaT,
            name=data.name,
            lastname=data.lastname,
            email=data.email,
            password=passwordHashed,
            phone=data.phone,
        )
        return user
    except Exception as error:
        raise error
