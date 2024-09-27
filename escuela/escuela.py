from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint


class Escuela:
    
    def __init__(self):
        self.lista_estudiantes: List[Estudiante] = []
        self.lista_maestros: List[Maestro] = []
        self.lista_materias: List[Materia] = []
        self.lista_grupos: List[Grupo] = []

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
    
    def listar_estudiante(self):
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
        return
    
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
            
    def listar_maestros(self):
            if not self.lista_maestros:
                print("No hay maestros registrados.")
            else:
                print("** MAESTROS **")
                for maestro in self.lista_maestros:
                    print(maestro.mostrar_info_maestro())
    
    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("MAESTRO ELIMINADO.")
                return
        print(f"No se encontró el maestro con el número de control: {numero_control}")



    def listar_materias(self):
        if not self.lista_materias:
            print("No hay materias registradas.")
        else:
            print("** MATERIAS **")
            for materia in self.lista_materias:
                print(materia.mostrar_info_materia())

    
    def eliminar_materia(self, numero_control_materia: str):
        for materia in self.lista_materias:
            if materia.numero_control == numero_control_materia:
                self.lista_materias.remove(materia)
                print("MATERIA ELIMINADA.")
                return
        print(f"No se encontró la materia con el número de control: {numero_control_materia}")

    

    






        

    



