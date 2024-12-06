from pydantic import BaseModel

class PatientModel(BaseModel):
    cedulaP: str
    name: str
    lastname: str
    phone: str
    cedulaT: str
