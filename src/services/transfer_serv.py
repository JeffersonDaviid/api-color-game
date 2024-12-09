from src.database import Transfer, Patient
from src.models.transfer_model import TransferModel
from src.utils.handle_respose import send_error_response


def create_session_serv(data: TransferModel):
    try:
        with Transfer._meta.database.atomic():
            transfer = Transfer.create(
                idTransfer=data.idTransfer,
                patient=data.patient,
                therapist_from=data.therapist_from,
                therapist_to=data.therapist_to,
                detail=data.detail,
                transfer_at=data.transfer_at,
            )
            patient = Patient.get_or_none(Patient.cedulaP == data.patient)
            if not patient:
                return send_error_response(404, "Paciente no encontrado")
            patient.cedulaT = data.therapist_to
            patient.save()
        return transfer
    except Exception as error:
        raise error
    
def get_transfers_therapist_from_serv(cedulaT: str):
    try:
        transfers = Transfer.select(
            Transfer.idTransfer,
            Transfer.patient,
            Transfer.therapist_from,
            Transfer.therapist_to,
            Transfer.detail,
            Transfer.transfer_at,
        ).where(Transfer.therapist_from == cedulaT)

        serialized_transfers = [
            {
                "idTransfer": transfer.idTransfer,
                "patient": transfer.patient.cedulaP,
                "therapist_from": transfer.therapist_from.cedulaT,
                "therapist_to": transfer.therapist_to.cedulaT,
                "detail": transfer.detail,
                "transfer_at": transfer.transfer_at.isoformat(),  # Convertir a formato ISO 8601
            }
            for transfer in transfers
        ]

        return serialized_transfers
    except Exception as error:
        raise error

def get_transfers_therapist_to_serv(cedulaT: str):
    try:
        transfers = Transfer.select(
            Transfer.idTransfer,
            Transfer.patient,
            Transfer.therapist_from,
            Transfer.therapist_to,
            Transfer.detail,
            Transfer.transfer_at,
        ).where(Transfer.therapist_to == cedulaT)

        # Serialización de los datos
        serialized_transfers = [
            {
                "idTransfer": transfer.idTransfer,
                "patient": transfer.patient.cedulaP,
                "therapist_from": transfer.therapist_from.cedulaT,
                "therapist_to": transfer.therapist_to.cedulaT,
                "detail": transfer.detail,
                "transfer_at": transfer.transfer_at.isoformat(),  # Convertir a formato ISO 8601
            }
            for transfer in transfers
        ]

        return serialized_transfers
    except Exception as error:
        raise error
    
def get_transfers_serv():
    try:
        transfers = Transfer.select(
            Transfer.idTransfer,
            Transfer.patient,
            Transfer.therapist_from,
            Transfer.therapist_to,
            Transfer.detail,
            Transfer.transfer_at,
        )
        
        serialized_transfers = [
            {
                "idTransfer": transfer.idTransfer,
                "patient": transfer.patient.cedulaP,
                "therapist_from": transfer.therapist_from.cedulaT,
                "therapist_to": transfer.therapist_to.cedulaT,
                "detail": transfer.detail,
                "transfer_at": transfer.transfer_at.isoformat(),  # Convertir a formato ISO 8601
            }
            for transfer in transfers
        ]
        
        return serialized_transfers
    except Exception as error:
        raise error