from src.services import therapist_serv


async def get_therapists_ctrl():
    therapists = await therapist_serv.get_therapists_serv()
    return therapists
