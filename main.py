from productos.productos import Producto
from excepciones.excepciones import ErrorProducto, ErrorPrecio, ErrorCantidad
import tkinter as tk
from tkinter import messagebox
from tienda.tienda import Tienda

Tienda=Tienda()

def ingresar_producto():
    try:
        nombre = entry_name.get()
        precio = float(entry_price.get())
        cantidad = int(entry_quantity.get())

        producto = Producto(nombre, precio, cantidad)
        Tienda.ingresar_producto(producto)
        

    except ErrorProducto as e:
        messagebox.showerror("Error", str(e))}
    except ErrorPrecio as e:
        messagebox.showerror("Error", str(e))
    except ErrorCantidad as e:
        messagebox.showerror("Error", str(e))




ventana = tk.Tk()
ventana.title("INVENTARIO TIENDA")
ventana.configure(bg="black")
ventana.geometry("400x200")

    
label_name = tk.Label(ventana, text="NOMBRE PRODUCTO",font=("Arial", 10, "bold"),bg="slategray")
label_name.grid(row=12,column=22)
entry_name = tk.Entry(ventana)
entry_name.grid(row=12,column=32)
label_price = tk.Label(ventana, text="PRECIO PRODUCTO",font=("Arial", 10, "bold"),bg="slategray")
label_price.grid(row=22,column=22)
entry_price = tk.Entry(ventana)
entry_price.grid(row=22,column=32)
label_quantity = tk.Label(ventana, text="CANTIDAD PRODUCTO",font=("Arial", 10, "bold"),bg="slategray")
label_quantity.grid(row=32,column=22)
entry_quantity = tk.Entry(ventana)
entry_quantity.grid(row=32,column=32)


boton_agregar=tk.Button(ventana, text="Agregar", command=ingresar_producto ,font=("arial",8),bg="ivory2")
boton_agregar.grid(row=52,column=22)



ventana.mainloop()