from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from semestre.semestre import Semestre
from random import randint

class Semestre:
    id: str
    numero: int
    materias: List[Materia]
    grupos: List[Grupo]
    numero_semestre: int

    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero = numero

    def generar_id(self, numero_semestre: int) -> str:
        id = f"{numero_semestre}-{randint(0, 10000)}-{randint(0, 10000)}"
        return id

    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)

    def mostrar_info_semestre(self):
        return (f"ID: {self.id}\n"
                f"Numero: {self.numero_semestre}\n"
                f"ID Carrera: {self.id_carrera}\n")