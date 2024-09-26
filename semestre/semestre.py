from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    id: str
    numero: int
    materias: List[Materia]
    grupos: List[Grupo]
    numero_semestre: int

def __init__(self, numero: int, id_carrera: str):
    self.id = self.generar_id(numero)

def generar_id(self, numero_semestre: int) -> str:
    id = f"{numero_semestre}-{randint(0, 10000)}-{randint(0, 10000)}"
    return id

