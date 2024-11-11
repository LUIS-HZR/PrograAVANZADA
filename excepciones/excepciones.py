import tkinter as tk
from tkinter import messagebox

class ErrorProducto(Exception):
    def __init__(self, mensaje="INGRESE DATOS VALIDOS"):
        self.mensaje=mensaje
        super().__init__(self.mensaje)

        
        
class ErrorPrecio(Exception):
    def __init__(self, mensaje="INGRESE DATOS VALIDOS"):
        self.mensaje=mensaje
        super().__init__(self.mensaje)
        
        
class ErrorCantidad(Exception):
    def __init__(self, mensaje="INGRESE DATOS VALIDOS"):
        self.mensaje=mensaje
        super().__init__(self.mensaje)
            
        


"""class Producto:
    nombre:str
    precio:float
    cantidad:int


    def __init__(self, nombre:str, precio:float, cantidad:int):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    def calcular_valor_total(self):
        valor_total=self.cantidad*self.precio
        return valor_total

    


def ingresar_precio(self, precio:float):
        try:
            precio = float(entry_price.get())

        except Errores as e:
            print(e)


def ingresar_nombre(self, nombre:float):
        try:
            nombre = str(entry_name.get())

        except Errores as e:
            print(e)


def ingresar_cantidad(self, cantidad:float):
        
        try:
            cantidad = int(entry_quantity.get())

        except Errores as e:
            print(e)


def agregar_producto(self,precio:float, cantidad, int):
    #try:


        #precio = int(entry_quantity.get())
        self.producto.calcular_valor_total(precio=precio, cantidad=cantidad)


        
        messagebox.showinfo("Inventario de producto: ", f"Cantidad: {cantidad}, Valor total: {valor_total}")"""

    #except Errores as e:
        #print(e)


#ventana = tk.Tk()
#ventana.title("INVENTARIO TIENDA")
#ventana.configure(bg="black")
#ventana.geometry("400x200")

    
#label_name = tk.Label(ventana, text="NOMBRE PRODUCTO",font=("Arial", 10, "bold"),bg="slategray")
#label_name.grid(row=12,column=22)
#entry_name = tk.Entry(ventana)
#entry_name.grid(row=12,column=32)


#boton_agregar=tk.Button(ventana, text="Agregar", command=agregar_producto ,font=("arial",8),bg="ivory2")
#boton_agregar.grid(row=52,column=22)

#ventana.mainloop()
