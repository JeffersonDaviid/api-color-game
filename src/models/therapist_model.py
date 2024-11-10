from pydantic import BaseModel


class TherapistModel(BaseModel):
    cedulaT: str
    name: str
    lastname: str
    email: str
    password: str
    phone: str
