from fastapi import APIRouter

from src.controllers import therapist_ctrl

therapist_router = APIRouter()


@therapist_router.get("/therapist/all")
async def get_therapist():
    return await therapist_ctrl.get_therapists_ctrl()
