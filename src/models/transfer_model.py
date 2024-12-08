from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TransferModel(BaseModel):
    idTransfer: int 
    patient: str 
    therapist_from: str 
    therapist_to: str 
    detail: Optional[str] 
    transfer_at: datetime 
        