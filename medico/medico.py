import random

class Medico:
    id: int
    nombre: str
    ano_nacimiento: int
    rfc: str
    direccion: str

    def __init__(self, nombre, ano_nacimiento, rfc, direccion):
        self.id = random.randint(1,100)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion

# @property
# def id(self):
#     return self.id
# @property
# def nombre(self):
#     return self.nombre
# @property
# def ano_nacimiento(self):
#     return self.ano_nacimiento
# @property
# def rfc(self):
#     return self.rfc
# @property
# def direccion(self):
#     return self.direccion

