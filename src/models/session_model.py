from pydantic import BaseModel, Field
from datetime import datetime

class SessionModel(BaseModel):
    idSesion: int 
    patient: str 
    therapist: str 
    num_corrects: int 
    num_incorrects: int 
    time_total: float 
    session_at: datetime 