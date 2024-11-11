
from excepciones.excepciones import ErrorProducto, ErrorPrecio, ErrorCantidad

class Producto:
    nombre:str
    precio:float
    cantidad:int


    def __init__(self, nombre:str, precio:float, cantidad:int):
        
        if nombre == "":
            raise ErrorProducto("Error")
        
        if precio<= 0:
            raise ErrorPrecio("Error")
        
        if cantidad< 0:
            raise ErrorCantidad("Error")


        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    def calcular_valor_total(self):
        valor_total=self.cantidad*self.precio
        return valor_total
    