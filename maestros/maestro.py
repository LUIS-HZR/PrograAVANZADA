class Maestro:
    numero_control_maestro: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float


    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float, numero_control_maestro: str):
        self.numero_control_maestro = numero_control_maestro
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        return (f"Número de control: {self.numero_control}\n"
                f"Nombre completo: {nombre_completo}\n"
                f"RFC: {self.rfc}\n"
                f"Sueldo: {self.sueldo}")