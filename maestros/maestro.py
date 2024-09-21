class Maestro:
    numero_control_maestro: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float


def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control_maestro: str):
    self.numero_control_maestro = numero_control_maestro
    self.nombre = nombre
    self.apellido = apellido
    self.rfc = rfc
    self.sueldo = sueldo
    