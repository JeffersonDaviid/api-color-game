from src.database import Therapist


async def get_therapists_serv():
    # users = await User.select()
    # for user in users:
    #     print(f"ID: {user.id}, Nombre: {user.name}, Edad: {user.age}")
    return {"user": 2, "nombre": "jefferson", "single": False}


def create_therapist_serv(name, age):
    user = Therapist.create(name=name, age=age)
    print(f"Usuario creado: {user.name}, Edad: {user.age}")
    return user
