from pydantic import BaseModel

class PatientModel(BaseModel):
    cedulaP: str
    cedulaT: str
    name: str
    lastname: str
    phone: str