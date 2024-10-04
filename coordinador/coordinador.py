from usuario.usuario import Usuario
from usuario.utils.roles import Rol
class Coordinador(Usuario):
    
    rfc: str
    sueldo: float
    anos_antiguedad: int


    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control: str, contrasenia:str, anos_antiguedad: int):
        super().__init__(numero_control=numero_control,nombre=nombre,apellido=apellido, contrasenia=contrasenia, rol=Rol)
        self.rfc = rfc
        self.sueldo = sueldo
        self.anos_antiguedad = anos_antiguedad
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        return (f"Número de control: {self.numero_control}\n"
                f"Nombre completo: {nombre_completo}\n"
                f"RFC: {self.rfc}\n"
                f"Sueldo: {self.sueldo}")
    
    