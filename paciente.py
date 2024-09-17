import random

class Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""

    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
        self.id = random.randint(1,100)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion

    def mostrar_informacion(self):
        print("ID: ", self.id)
        print(f"NOMBRE: {self.nombre}")
        print(f"AÑO DE NACIMIENTO: {self.ano_nacimiento}")
        print(f"PESO: {self.peso}")
        print(f"ESTATURA: {self.estatura}")
        print(f"DIRECCION: {self.direccion}")

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
# def estatura(self):
#     return self.estatura
# @property
# def peso(self):
#     return self.peso
# @property
# def direccion(self):
#     return self.direccion

