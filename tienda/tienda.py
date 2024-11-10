from productos.productos import Producto
from excepciones.excepciones import ErrorProducto
from typing import List
from tkinter import messagebox


class Tienda:

    def __init__(self):
        self.productos: List[Producto]=[]
    
    def ingresar_producto(self, producto:Producto):
        self.productos.append(producto)
        
        messagebox.showinfo(f"Nombre del producto: {producto.nombre}")
            
    def listar_inventario(self):

        for producto in self.productos:
            messagebox.showinfo(f"Nombre del producto: {producto}")

    def calcular_inventario(self, producto:Producto):
        valor_total=producto.calcular_valor_total()
        return valor_total




    #def ingresar_precio(self, precio:float):
        #try:
            #precio = float(entry_price.get())

        #except Errores as e:
            #print(e)

        


        


