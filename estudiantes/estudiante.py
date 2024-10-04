from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Estudiante(Usuario):
    curp: str
    fecha_nacimiento: datetime


    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contrasenia:str):
        super().__init__(numero_control=numero_control,nombre=nombre,apellido=apellido, contrasenia=contrasenia,rol=Rol.ESTUDIANTE)
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        
    
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre}{self.apellido}"
        info = f"Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, Curp: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento}"
        return info

    

