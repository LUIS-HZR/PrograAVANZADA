from typing import List
from datetime import datetime
from visitantes.visitantes import Visitante
from empleado.empleado import Empleado


class Zoologico():
    
    def __init__(self):
        self.lista_visitantes: List[Visitante]
        self.lista_empleados: List[Empleado]

    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)

    def registrar_empleado(self, empleado: Empleados):
        self.lista_empleados.append(empleado)

    def registrar_visita(self):
        pass
    def registrar_animal(self):
        pass
    def registrar_mantenimiento(self):
        pass
    def modificar_datos_empleado(self):
        pass
    def modificar_datos_visitante(self):
        pass
    def modificar_datos_animal(self):
        pass
    def eliminar_empleado(self):
        pass
    def eliminar_visitante(self):
        pass
    def eliminar_animal(self):
        pass
    def mostrar_empleados(self):
        pass
    def mostrar_visitantes(self):
        pass
    def mostrar_animal(self):
        pass
    def mostrar_visitas(self):
        pass
    def mostrar_mantenimiento(self):
        pass


    def listar_visitantes(self):
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
        return

        