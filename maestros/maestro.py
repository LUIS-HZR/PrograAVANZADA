from usuario.usuario import Usuario
from usuario.utils.roles import Rol
class Maestro(Usuario):
    
    rfc: str
    sueldo: float


    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str, contrasenia:str):
        super().__init__(numero_control=numero_control,nombre=nombre,apellido=apellido, contrasenia=contrasenia, rol=Rol)
        self.rfc = rfc
        self.sueldo = sueldo
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        return (f"Número de control: {self.numero_control}\n"
                f"Nombre completo: {nombre_completo}\n"
                f"RFC: {self.rfc}\n"
                f"Sueldo: {self.sueldo}")