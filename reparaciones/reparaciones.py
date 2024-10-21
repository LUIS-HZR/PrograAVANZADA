from datetime import datetime
from typing import List 
from mantenimiento.mantenimiento import Mantenimiento

class Reparaciones:
    empleado_encargado: List[Mantenimiento] =[]
    proceso_realizado: str
    observaciones: str
    id_animal: str
    fecha_proceso: datetime
    
    def __init__(self,empleado_encargado: str,proceso_realizado: str,observaciones: str,id_animal: str,fecha_proceso: datetime):
        self.empleado_encargado = empleado_encargado
        self.proceso_realizado = proceso_realizado
        self.observaciones = observaciones
        self.id_animal = id_animal
        self.fecha_proceso = fecha_proceso
    
    def mostrar_info_mantenimiento(self):
        info = f"- Empleado a cargo: {self.empleado_encargado}\n- Proceso: {self.proceso_realizado}\n- Observaciones: {self.observaciones}\n- ID del animal: {self.id_animal}\n- Fecha del proceso: {self.fecha_proceso}\n"
        return info