from datetime import datetime
from urllib.parse import urlparse

from decouple import config
from peewee import (
    CharField,
    DateTimeField,
    FloatField,
    ForeignKeyField,
    IntegerField,
    Model,
    PostgresqlDatabase,
)

DATABASE_URL = config("DATABASE_URL")
# Parsea la URL de conexión
url = urlparse(DATABASE_URL)
db_params = {
    "database": url.path[1:],  # Ignorar el primer "/" en la ruta
    "user": url.username,
    "password": url.password,
    "host": url.hostname,
    "port": url.port,
}
db = PostgresqlDatabase(**db_params)


# Modelo base
class BaseModel(Model):
    class Meta:
        database = db


# Modelo de Terapeuta
class Therapist(BaseModel):
    cedulaT = CharField(primary_key=True)
    name = CharField()
    lastname = CharField()
    email = CharField()
    password = CharField()
    phone = CharField()


# Modelo de Paciente
class Patient(BaseModel):
    cedulaP = CharField(primary_key=True)
    name = CharField()
    lastname = CharField()
    phone = CharField()
    cedulaT = ForeignKeyField(Therapist, backref="patients", on_delete="CASCADE")


# Modelo de Sesión
class Session(BaseModel):
    idSesion = IntegerField(primary_key=True)  # Definir como clave primaria
    patient = ForeignKeyField(
        Patient, backref="sessions", on_delete="CASCADE"
    )  # Relación de clave foránea con Paciente
    therapist = ForeignKeyField(
        Therapist, backref="sessions", on_delete="CASCADE"
    )  # Relación de clave foránea con Terapeuta
    num_corrects = IntegerField()
    num_incorrects = IntegerField()
    time_total = FloatField()
    session_at = DateTimeField(default=datetime.now)


# Modelo de Transferencia
class Transfer(BaseModel):
    idTransfer = IntegerField(primary_key=True)  # Definir como clave primaria
    patient = ForeignKeyField(
        Patient, backref="transfers", on_delete="CASCADE"
    )  # Relación de clave foránea con Paciente
    therapist_from = ForeignKeyField(
        Therapist, backref="transfers_from", on_delete="CASCADE"
    )  # Relación de clave foránea con Terapeuta (origen)
    therapist_to = ForeignKeyField(
        Therapist, backref="transfers_to", on_delete="CASCADE"
    )  # Relación de clave foránea con Terapeuta (destino)
    detail = CharField()
    transfer_at = DateTimeField(default=datetime.now)


# Conectar y crear la tabla si no existe
db.connect()
db.create_tables([Therapist, Patient, Session, Transfer], safe=True)
