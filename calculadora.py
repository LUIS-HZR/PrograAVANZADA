import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicacion es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")




ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x400")

label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=20)
boton_sumar = tk.Button(ventana, text="Restar", command=restar)
boton_sumar.pack(pady=20)
boton_sumar = tk.Button(ventana, text="Dividir", command=dividir)
boton_sumar.pack(pady=20)
boton_sumar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_sumar.pack(pady=20)


ventana.mainloop()