from pydantic import BaseModel


class AuthModel(BaseModel):
    cedulaT: str
    password: str
