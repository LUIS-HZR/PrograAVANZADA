import tkinter as tk
import mysql.connector
from tkinter import ttk, messagebox
from tkinter import *

def verificar_usuario(usuario, contraseña):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='proyecto'
        )
        cursor = conn.cursor()


        cursor.execute('''
            SELECT rol FROM usuarios1 WHERE Usuario = %s AND Contraseña = %s
        ''', (usuario, contraseña))
        
        rol = cursor.fetchone()  

   
        print(f"Resultado de la consulta: {rol}")

        if rol:
            return rol[0]  
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
            return None
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
        return None
    finally:
        if conn.is_connected():
            conn.close()

def ventana_Login():
    def login():
        usuario = entry_correo.get().strip()
        contraseña = entry_contraseña.get().strip()

        print(f"Intentando iniciar sesión con Usuario: '{usuario}', Contraseña: '{contraseña}'")


        rol_verificar = verificar_usuario(usuario, contraseña)

        if rol_verificar:
            print(f"Rol obtenido: {rol_verificar}")
        else:
            print("No se obtuvo un rol válido.")

        if rol_verificar == "administrador":
            ventanaP.withdraw()

            
            def mostrarUsuarios():
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                micursos.execute("select * from usuarios1")
                lista = micursos.fetchall()

                for i,(id,Nombre,Apellido,Usuario,Contraseña, rol) in enumerate(lista,start=1):
                    listbox.insert("","end",values=(id,Nombre,Apellido,Usuario,Contraseña, rol))
                    mysqlC.close()

            def agregarUsuarios():
                nombreAdd = Nombre.get()
                apellidoAdd = Apellido.get()
                usuarioAdd = Usuario.get()
                contraAdd = Contraseña.get()
                rolAdd = rol.get()
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                try:
                    micursos.execute(f"insert into usuarios1(Nombre,Apellido,Usuario,Contraseña,Rol) values('{nombreAdd}','{apellidoAdd}','{usuarioAdd}','{contraAdd}','{rolAdd}')")
                    mysqlC.commit()
                    Nombre.delete(0,END)
                    Apellido.delete(0,END)
                    Usuario.delete(0,END)
                    Contraseña.delete(0,END)
                    rol.delete(0,END)
                    messagebox.showinfo("informacion","usuario agregado")
                    actualizarU()
                except Exception as e:
                    print(e)
                    mysqlC.rollback()
                    mysqlC.close()

            def actualizarU():
                for i in listbox.get_children():
                    listbox.delete(i)
                mostrarUsuarios()

            def editarUsuarios():
                nombreAdd = Nombre.get()
                apellidoAdd = Apellido.get()
                usuarioAdd = Usuario.get()
                contraAdd = Contraseña.get()
                rolAdd = rol.get()
                idAdd = idA.get()
                
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                try:
                    micursos.execute(f"UPDATE usuarios1 set Nombre='{nombreAdd}',Apellido='{apellidoAdd}',Usuario='{usuarioAdd}',Contraseña='{contraAdd}',rol='{rolAdd}' where Nombre='{nombreAdd}'")
                    mysqlC.commit()
                    Nombre.delete(0,END)
                    Apellido.delete(0,END)
                    Usuario.delete(0,END)
                    Contraseña.delete(0,END)
                    rol.delete(0,END)
                    messagebox.showinfo("informacion","usuario editado")
                    actualizarU()
                except Exception as e:
                    print(e)
                    mysqlC.rollback()
                    mysqlC.close()

            def eliminarUsuarios():
                idAdd = idA.get()
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                try:
                    micursos.execute(f"DELETE FROM usuarios1 WHERE Id={idAdd}")
                    mysqlC.commit()
                    Nombre.delete(0,END)
                    Apellido.delete(0,END)
                    Usuario.delete(0,END)
                    Contraseña.delete(0,END)
                    rol.delete(0,END)
                    messagebox.showinfo("informacion","usuario eliminado")
                    actualizarU()
                except Exception as e:
                    print(e)
                    mysqlC.rollback()
                    mysqlC.close()

            def obtenerR(event):
                Nombre.delete(0,END)
                Apellido.delete(0,END)
                Usuario.delete(0,END)
                Contraseña.delete(0,END)
                rol.delete(0,END)


                renglon = listbox.selection()[0]
                print(renglon)
                seleccion = listbox.set(renglon)
                print(seleccion)
                
                Nombre.insert(0,seleccion["Nombre"])
                Apellido.insert(0,seleccion["Apellido"])
                Usuario.insert(0,seleccion["Usuario"])
                Contraseña.insert(0,seleccion["Contraseña"])
                rol.insert(0,seleccion["rol"])

            def regresar_a_login():
                ventanaUsuarios.destroy()  
                ventanaP.deiconify()
                #boton_regresar_login = tk.Button(ventana_usuarios, text="Salir", command=regresar_a_login)
                #boton_regresar_login.pack(pady=20)

            def abrirVentanaLibros():
                ventanaUsuarios.withdraw()
                
                def mostrar():
                    mysqlC = mysql.connector.connect(host='localhost',user='root',password='',database='proyecto')
                    micursos=mysqlC.cursor()
                    micursos.execute("select * from libros1")
                    lista = micursos.fetchall()

                    for i,(id,titulo,autor,editorial,año_publicacion,precio ) in enumerate(lista,start=1):
                        listbox.insert("","end",values=(id,titulo,autor,editorial,año_publicacion,precio))
                        mysqlC.close()

                def agregar():
                    tituloAdd = titulo.get()
                    autorAdd = autor.get()
                    editorialAdd = editorial.get()
                    añoAdd = año.get()
                    precioAdd = precio.get()
                    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                    micursos=mysqlC.cursor()
                    try:
                        micursos.execute(f"insert into libros1(titulo, autor, editorial, año_publicacion, precio) values('{tituloAdd}','{autorAdd}','{editorialAdd}','{añoAdd}', '{precioAdd}')")
                        mysqlC.commit()
                        titulo.delete(0,END)
                        autor.delete(0,END)
                        editorial.delete(0,END)
                        año.delete(0,END)
                        precio.delete(0,END)
                        messagebox.showinfo("informacion","libro agregado")
                        actualizar()
                    except Exception as e:
                        print(e)
                        mysqlC.rollback()
                        mysqlC.close()

                def actualizar():
                    for i in listbox.get_children():
                        listbox.delete(i)
                    mostrar()

                def editar():
                    tituloAdd = titulo.get()
                    autorAdd = autor.get()
                    editorialAdd = editorial.get()
                    añoAdd = año.get()
                    precioAdd = precio.get()
                    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                    micursos=mysqlC.cursor()
                    try:
                        micursos.execute(f"UPDATE libros1 set autor='{autorAdd}',editorial='{editorialAdd}', año_publicacion='{añoAdd}', precio='{precioAdd}' where titulo='{tituloAdd}'")
                        mysqlC.commit()
                        titulo.delete(0,END)
                        autor.delete(0,END)
                        editorial.delete(0,END)
                        año.delete(0,END)
                        precio.delete(0, END)
                        messagebox.showinfo("informacion","usuario editado")
                        actualizar()
                    except Exception as e:
                        print(e)
                        mysqlC.rollback()
                        mysqlC.close()

                def eliminar():
                    tituloAdd = titulo.get()
                    mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                    micursos=mysqlC.cursor()
                    try:
                        micursos.execute(f"DELETE FROM libros1 WHERE titulo='{tituloAdd}'")

                        mysqlC.commit()
                        titulo.delete(0,END)
                        autor.delete(0,END)
                        editorial.delete(0,END)
                        año.delete(0,END)
                        precio.delete(0,END)
                        messagebox.showinfo("informacion","libro eliminado")
                        actualizar()
                    except Exception as e:
                        print(e)
                        mysqlC.rollback()
                        mysqlC.close()

                def obtenerRenglon(event):
                    titulo.delete(0,END)
                    autor.delete(0,END)
                    editorial.delete(0,END)
                    año.delete(0,END)
                    precio.delete(0,END)
                    precio.delete(0,END)

                    renglon = listbox.selection()[0]
                    print(renglon)
                    seleccion = listbox.set(renglon)
                    print(seleccion)
                    titulo.insert(0,seleccion["Titulo"])
                    autor.insert(0,seleccion["Autor"])
                    editorial.insert(0,seleccion["Editorial"])
                    año.insert(0,seleccion["Año"])
                    precio.insert(0, seleccion["Precio"])

                def filtrar_por_editorial():
                    editorialFiltro = editFiltro.get()
                    for i in listbox.get_children():
                        listbox.delete(i)

                    mysqlC = mysql.connector.connect(host='localhost', user='root', password='', database='proyecto')
                    micursos = mysqlC.cursor()
                    try:
                        micursos.execute(f"SELECT * FROM libros1 WHERE editorial='{editorialFiltro}'")
                        lista = micursos.fetchall()

                        for i, (id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
                            listbox.insert("", "end", values=(id, titulo, autor, editorial, año_publicacion, precio))
                    except Exception as e:
                        print(e)
                        messagebox.showerror("Error", "No se pudo filtrar los libros.")
                    finally:
                        mysqlC.close()

                def regresar_a_login():
                    ventanaLibros.destroy()  
                    ventanaP.deiconify()

                def regresarVentanaUsuarios():
                    ventanaLibros.destroy()  
                    ventanaUsuarios.deiconify()

                ventanaLibros = tk.Toplevel(ventanaUsuarios)
                ventanaLibros.geometry("1200x700")

                label1 = tk.Label(ventanaLibros,text="Registro de libros", fg="red",font=("Arial",28)).place(x=370,y=0)

                global titulo
                global autor
                global editorial
                global año
                global precio


                labeltitulo = tk.Label(ventanaLibros, text="Titulo", font=("Arial", 12))
                labeltitulo.place(x=400, y=80)

                labelautor = tk.Label(ventanaLibros, text="Autor", font=("Arial", 12))
                labelautor.place(x=400, y=110)

                labeleditorial = tk.Label(ventanaLibros, text="Editorial", font=("Arial", 12))
                labeleditorial.place(x=400, y=140)

                labelaño = tk.Label(ventanaLibros, text="Año", font=("Arial", 12))
                labelaño.place(x=400, y=170)

                labelprecio = tk.Label(ventanaLibros, text="Precio", font=("Arial", 12))
                labelprecio.place(x=400, y=200)

                labeleditFiltro = tk.Label(ventanaLibros, text="Editorial", font=("Arial", 12))
                labeleditFiltro.place(x=850, y=300)

                titulo = tk.Entry(ventanaLibros)
                titulo.place(x=500, y=80)

                autor = tk.Entry(ventanaLibros)
                autor.place(x=500, y=110)

                editorial= tk.Entry(ventanaLibros)
                editorial.place(x=500, y=140)

                año = tk.Entry(ventanaLibros)
                año.place(x=500, y=170)

                precio = tk.Entry(ventanaLibros)
                precio.place(x=500, y=200)

                editFiltro = tk.Entry(ventanaLibros)
                editFiltro.place(x=1000, y=300)

                tk.Button(ventanaLibros,text="Crear",command=agregar, height=5, width=10, font=("Arial",12)).place(x=250,y=80)
                tk.Button(ventanaLibros,text="Editar",command=editar, height=5, width=10, font=("Arial",12)).place(x=700,y=80)
                tk.Button(ventanaLibros,text="Eliminar",command=eliminar, height=5, width=10, font=("Arial",12)).place(x=250,y=200)
                tk.Button(ventanaLibros,text="Salir a Login",command=regresar_a_login, height=2, width=20, font=("Arial",8)).place(x=1000,y=50)
                tk.Button(ventanaLibros,text="Regresar Ventana Usuarios",command=regresarVentanaUsuarios, height=2, width=20, font=("Arial",7)).place(x=1000,y=100)
                tk.Button(ventanaLibros,text="Filtrar Editorial",command=filtrar_por_editorial, height=2, width=12, font=("Arial",8)).place(x=1000,y=230)
                tk.Button(ventanaLibros,text="Mostrar Todo",command=mostrar, height=2, width=10, font=("Arial",8)).place(x=900,y=230)

                columnas = ("Id","Titulo","Autor","Editorial","Año","Precio") 
                listbox = ttk.Treeview(ventanaLibros,columns=columnas,show="headings")

                for col in columnas:
                    listbox.heading(col, text=col)
                    listbox.grid(row=1, column=0, columnspan=1)
                    listbox.place(x=0, y=350)

                mostrar()
                listbox.bind("<Double-Button-1>",obtenerRenglon)


                ventanaLibros.mainloop()


            ventanaUsuarios = tk.Toplevel(ventanaP)
            ventanaUsuarios.geometry("1200x700")
            label1 = tk.Label(ventanaUsuarios,text="Registro de usuarios", fg="red",font=("Arial",28)).place(x=170,y=0)

            global Nombre
            global Apellido
            global Usuario
            global Contraseña
            global rol


            labelnombre = tk.Label(ventanaUsuarios, text="Nombre", font=("Arial", 12))
            labelnombre.place(x=100, y=50)

            labelapellido = tk.Label(ventanaUsuarios, text="Apellido", font=("Arial", 12))
            labelapellido.place(x=100, y=80)

            labelUsuario = tk.Label(ventanaUsuarios, text="Correo", font=("Arial", 12))
            labelUsuario.place(x=100, y=110)

            labelcontrasena = tk.Label(ventanaUsuarios, text="Contraseña", font=("Arial", 12))
            labelcontrasena.place(x=100, y=140)

            labelrol = tk.Label(ventanaUsuarios, text="rol", font=("Arial", 12))
            labelrol.place(x=100, y=170)

            labelidA = tk.Label(ventanaUsuarios, text="ID", font=("Arial", 12))
            labelidA.place(x=650, y=170)

            Nombre = tk.Entry(ventanaUsuarios)
            Nombre.place(x=270, y=50)

            Apellido = tk.Entry(ventanaUsuarios)
            Apellido.place(x=270, y=80)

            Usuario = tk.Entry(ventanaUsuarios)
            Usuario.place(x=270, y=110)

            Contraseña = tk.Entry(ventanaUsuarios)
            Contraseña.place(x=270, y=140)

            rol = tk.Entry(ventanaUsuarios)
            rol.place(x=270, y=170)

            idA = tk.Entry(ventanaUsuarios)
            idA.place(x=680, y=170)

            tk.Button(ventanaUsuarios,text="Crear",command=agregarUsuarios, height=5, width=10, font=("Arial",12)).place(x=140,y=220)
            tk.Button(ventanaUsuarios,text="Editar",command=editarUsuarios, height=5, width=10, font=("Arial",12)).place(x=700,y=220)
            tk.Button(ventanaUsuarios,text="Eliminar",command=eliminarUsuarios, height=5, width=10, font=("Arial",12)).place(x=300,y=220)
            tk.Button(ventanaUsuarios,text="Salir a Login",command=regresar_a_login, height=2, width=20, font=("Arial",8)).place(x=1000,y=50)
            tk.Button(ventanaUsuarios,text="Registro Libros",command=abrirVentanaLibros, height=2, width=20, font=("Arial",8)).place(x=1000,y=100)
            


            
            columnas = ("Id","Nombre","Apellido","Usuario","Contraseña","rol")
            listbox = ttk.Treeview(ventanaUsuarios,columns=columnas,show="headings")

            for col in columnas:
                listbox.heading(col, text=col)
                listbox.grid(row=1, column=0, columnspan=1)
                listbox.place(x=0, y=400)

            mostrarUsuarios()
            listbox.bind("<Double-Button-1>",obtenerR)

            ventanaUsuarios.mainloop()
              
            
        elif rol_verificar == "Empleado":
            ventanaP.withdraw()
            ventanaLibros = tk.Toplevel(ventanaP)
            ventanaLibros.geometry("1200x700")

            label1 = tk.Label(ventanaLibros,text="Registro de libros", fg="red",font=("Arial",28)).place(x=370,y=0)

            def mostrar():
                mysqlC = mysql.connector.connect(host='localhost',user='root',password='',database='proyecto')
                micursos=mysqlC.cursor()
                micursos.execute("select * from libros1")
                lista = micursos.fetchall()

                for i,(id,titulo,autor,editorial,año_publicacion,precio ) in enumerate(lista,start=1):
                    listbox.insert("","end",values=(id,titulo,autor,editorial,año_publicacion,precio))
                    mysqlC.close()

            def agregar():
                tituloAdd = titulo.get()
                autorAdd = autor.get()
                editorialAdd = editorial.get()
                añoAdd = año.get()
                precioAdd = precio.get()
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                try:
                    micursos.execute(f"insert into libros1(titulo, autor, editorial, año_publicacion, precio) values('{tituloAdd}','{autorAdd}','{editorialAdd}','{añoAdd}', '{precioAdd}')")
                    mysqlC.commit()
                    titulo.delete(0,END)
                    autor.delete(0,END)
                    editorial.delete(0,END)
                    año.delete(0,END)
                    precio.delete(0,END)
                    messagebox.showinfo("informacion","libro agregado")
                    actualizar()
                except Exception as e:
                    print(e)
                    mysqlC.rollback()
                    mysqlC.close()

            def actualizar():
                for i in listbox.get_children():
                    listbox.delete(i)
                mostrar()

            def editar():
                tituloAdd = titulo.get()
                autorAdd = autor.get()
                editorialAdd = editorial.get()
                añoAdd = año.get()
                precioAdd = precio.get()
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                try:
                    micursos.execute(f"UPDATE libros1 set autor='{autorAdd}',editorial='{editorialAdd}', año_publicacion='{añoAdd}', precio='{precioAdd}' where titulo='{tituloAdd}'")
                    mysqlC.commit()
                    titulo.delete(0,END)
                    autor.delete(0,END)
                    editorial.delete(0,END)
                    año.delete(0,END)
                    precio.delete(0, END)
                    messagebox.showinfo("informacion","usuario editado")
                    actualizar()
                except Exception as e:
                    print(e)
                    mysqlC.rollback()
                    mysqlC.close()

            def eliminar():
                tituloAdd = titulo.get()
                mysqlC = mysql.connector.connect(host="localhost",user="root",password="",database="proyecto")
                micursos=mysqlC.cursor()
                try:
                    micursos.execute(f"DELETE FROM libros1 WHERE titulo='{tituloAdd}'")

                    mysqlC.commit()
                    titulo.delete(0,END)
                    autor.delete(0,END)
                    editorial.delete(0,END)
                    año.delete(0,END)
                    precio.delete(0,END)
                    messagebox.showinfo("informacion","libro eliminado")
                    actualizar()
                except Exception as e:
                    print(e)
                    mysqlC.rollback()
                    mysqlC.close()

            def obtenerRenglon(event):
                titulo.delete(0,END)
                autor.delete(0,END)
                editorial.delete(0,END)
                año.delete(0,END)
                precio.delete(0,END)
                precio.delete(0,END)

                renglon = listbox.selection()[0]
                print(renglon)
                seleccion = listbox.set(renglon)
                print(seleccion)
                titulo.insert(0,seleccion["Titulo"])
                autor.insert(0,seleccion["Autor"])
                editorial.insert(0,seleccion["Editorial"])
                año.insert(0,seleccion["Año"])
                precio.insert(0, seleccion["Precio"])

            def regresar_a_login():
                ventanaLibros.destroy()  
                ventanaP.deiconify()


            

            def filtrar_por_editorial():
                editorialFiltro = editFiltro.get()
                for i in listbox.get_children():
                    listbox.delete(i)

                mysqlC = mysql.connector.connect(host='localhost', user='root', password='', database='proyecto')
                micursos = mysqlC.cursor()
                try:
                    micursos.execute(f"SELECT * FROM libros1 WHERE editorial='{editorialFiltro}'")
                    lista = micursos.fetchall()

                    for i, (id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
                        listbox.insert("", "end", values=(id, titulo, autor, editorial, año_publicacion, precio))
                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", "No se pudo filtrar los libros.")
                finally:
                    mysqlC.close()

            

            global titulo
            global autor
            global editorial
            global año
            global precio


            labeltitulo = tk.Label(ventanaLibros, text="Titulo", font=("Arial", 12))
            labeltitulo.place(x=400, y=80)

            labelautor = tk.Label(ventanaLibros, text="Autor", font=("Arial", 12))
            labelautor.place(x=400, y=110)

            labeleditorial = tk.Label(ventanaLibros, text="Editorial", font=("Arial", 12))
            labeleditorial.place(x=400, y=140)

            labelaño = tk.Label(ventanaLibros, text="Año", font=("Arial", 12))
            labelaño.place(x=400, y=170)

            labelprecio = tk.Label(ventanaLibros, text="Precio", font=("Arial", 12))
            labelprecio.place(x=400, y=200)

            labeleditFiltro = tk.Label(ventanaLibros, text="Editorial", font=("Arial", 12))
            labeleditFiltro.place(x=850, y=300)



            editFiltro = tk.Entry(ventanaLibros)
            editFiltro.place(x=1000, y=300)



            titulo = tk.Entry(ventanaLibros)
            titulo.place(x=500, y=80)

            autor = tk.Entry(ventanaLibros)
            autor.place(x=500, y=110)

            editorial= tk.Entry(ventanaLibros)
            editorial.place(x=500, y=140)

            año = tk.Entry(ventanaLibros)
            año.place(x=500, y=170)

            precio = tk.Entry(ventanaLibros)
            precio.place(x=500, y=200)

            tk.Button(ventanaLibros,text="Crear",command=agregar, height=5, width=10, font=("Arial",12)).place(x=250,y=80)
            tk.Button(ventanaLibros,text="Editar",command=editar, height=5, width=10, font=("Arial",12)).place(x=700,y=80)
            tk.Button(ventanaLibros,text="Eliminar",command=eliminar, height=5, width=10, font=("Arial",12)).place(x=250,y=200)
            tk.Button(ventanaLibros,text="Filtrar Editorial",command=filtrar_por_editorial, height=2, width=10, font=("Arial",8)).place(x=1000,y=230)
            tk.Button(ventanaLibros,text="Mostrar Todo",command=mostrar, height=2, width=10, font=("Arial",8)).place(x=900,y=230)

            tk.Button(ventanaLibros,text="Salir a Login",command=regresar_a_login, height=2, width=20, font=("Arial",8)).place(x=1000,y=50)

            columnas = ("Id","Titulo","Autor","Editorial","Año","Precio")
            listbox = ttk.Treeview(ventanaLibros,columns=columnas,show="headings")

            for col in columnas:
                listbox.heading(col, text=col)
                listbox.grid(row=1, column=0, columnspan=1)
                listbox.place(x=0, y=350)

            mostrar()
            listbox.bind("<Double-Button-1>",obtenerRenglon)


            ventanaLibros.mainloop()
            
        else:
            messagebox.showerror("Error", "Rol no reconocido o credenciales incorrectas.")

    ventanaP = tk.Tk()
    ventanaP.title("Login")
    ventanaP.geometry("300x200")
    
    label_correo = tk.Label(ventanaP, text="Correo:")
    label_correo.pack(pady=5)
    entry_correo = tk.Entry(ventanaP, width=30)
    entry_correo.pack(pady=5)
    
    label_contraseña = tk.Label(ventanaP, text="Contraseña:")
    label_contraseña.pack(pady=5)
    entry_contraseña = tk.Entry(ventanaP, width=30, show="*")
    entry_contraseña.pack(pady=5)
    
    btn_login = tk.Button(ventanaP, text="Login", command=login)
    btn_login.pack(pady=20)
    
    ventanaP.mainloop()

ventana_Login()