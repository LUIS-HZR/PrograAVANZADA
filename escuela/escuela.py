from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint


class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_grupos: List[Grupo] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        numero_control = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(1, 1000)}"
        return numero_control
    
    def registrar_maestro(self, maestro:Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestro(self, nombre, rfc, ano_nacimiento):
        digitos_rfc=rfc[-2:].upper()
        digitos_nombre=nombre[0:2].upper()
        dia=datetime.now().day
        numero_control_maestro = f"M{ano_nacimiento}{dia}{randint(500, 5000)}{digitos_nombre}{digitos_rfc}{len(self.lista_estudiantes) + 1}"
        return numero_control_maestro

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)


    def generar_id_materia(self, nombre, semestre, creditos):
        digitos_nombre=nombre[-2:].upper()
        id = f"MT{digitos_nombre}{semestre}{creditos}"
        return id
    
    
    






        

    



