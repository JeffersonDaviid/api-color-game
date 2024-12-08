from fastapi import APIRouter

from src.services.transfer_serv import create_session_serv, get_transfers_therapist_from_serv, get_transfers_therapist_to_serv,get_transfers_serv
from src.utils.error_handle import get_details_error
from src.utils.handle_respose import send_success_response
from src.models.transfer_model import TransferModel


transfer_router = APIRouter()

@transfer_router.post("/register")
def post_transfer_ctrl(data: TransferModel):
    try:
        print(f"Datos recibidos en el backend-: {data.dict()}")
        transfer = create_session_serv(data)
        print(f"Transferencia creada: {transfer.idTransfer}")
        return send_success_response(201, "Transferencia creada")
    except Exception as error:
        return get_details_error(error)
    

@transfer_router.get("/from/{cedulaT}")
def get_transfers_therapist_from_ctrl(cedulaT: str):
    try:
        transfers = get_transfers_therapist_from_serv(cedulaT=cedulaT)

        if not transfers:
            return send_success_response(200, "No existen transferencias para este terapeuta")

        return send_success_response(200, "Transferencias hechas por este terapeuta", transfers)  
    except Exception as error:
        return get_details_error(error)
    
@transfer_router.get("/to/{cedulaT}")
def get_transfers_therapist_to_ctrl(cedulaT: str):
    try:
        transfers = get_transfers_therapist_to_serv(cedulaT=cedulaT)

        if not transfers:
            return send_success_response(200, "No existen transferencias para este terapeuta")

        return send_success_response(200, "Transferencias recibidas para este terapeuta", transfers)
    except Exception as error:
        return get_details_error(error)
    
@transfer_router.get("/all")
def get_transfers_ctrl():
    try:
        transfers = get_transfers_serv()

        if not transfers:
            return send_success_response(200, "No hay transferencias registradas")

        return send_success_response(200, "Todas las transferencias registradas", transfers)
    except Exception as error:
        return get_details_error(error)
    