from usuario.utils.roles import Rol
from datetime import datetime
from empleados.empleados import Empleado

class Veterinario(Empleado):
    
    def __init__(self,nombre: str, apellido: str, id: str, curp: str, fecha_nacimiento: datetime, fecha_ingreso: datetime, rfc: str, salario: float,horario: str):
        super().__init__(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc, salario=salario,horario=horario, rol=Rol.VETERINARIO)
        pass
    