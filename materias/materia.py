class Materia:
    id: str #ID = "MT"{ultimos dos digitos del nombre}{semestre}{cantidad creditos}
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    

    def __init__(self, nombre: str, descripcion: str, semestre: int, creditos: int, id: str ):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos


    def mostrar_info_materia(self):
        return (f"Número de control: {self.numero_control}\n"
                f"Nombre: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Semestre: {self.semestre}\n"
                f"Créditos: {self.creditos}")
    
    