from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo




class Menu:
    escuela= Escuela()

    usuario_estudiante:str = "luison123"
    contrasenia_estudiante:str = "12345*"
    usuario_maestro:str = "eder123"
    contrasenia_maestro:str = "54321*"


    def login(self):

        intentos = 0
        while intentos < 5:

            print("-----------------BIENVENIDO-------------------------")
            print("Inicia sesion para continuar")

            nombre_usuario = input("Ingresa tu nombre de usuario")
            contrasenia_usuario = input("Ingresña tu contraseña")

            if nombre_usuario == self.usuario_estudiante:
                if contrasenia_usuario == self.contrasenia_estudiante:
                    self.mostrar_menu_estudiante()

                else:
                    intentos += 1
                    print("\n USUARIO O CONTRASEÑA INCORRECTOS")
            elif nombre_usuario == self.usuario_maestro:
                if contrasenia_usuario == self.contrasenia_maestro:
                    self.mostrar_menu_maestro()

                else:
                    intentos += 1
                    print("\n USUARIO O CONTRASEÑA INCORRECTOS")

    def mostrar_menu_estudiante(self):
        pass
    def mostrar_menu_maestro(self):
        pass

    def mostrar_menu(self):
        while True:

    
            print("-------------------------Mindbox-------------------------------------")
            print("1. REGISTRAR ESTUDIANTE")
            print("2. REGISTRAR MAESTRO")
            print("3. REGISTRAR MATERIA")
            print("4. REGISTRAR GRUPO")
            print("5. REGISTRAR HORARIO")
            print("6. MOSTRAR ESTUDIANTES")
            print("7. MOSTRAR MAESTROS")
            print("8. MOSTRAR MATERIAS")
            print("9. MOSTRA        R GRUPOS")
            print("10. ELIMINAR ESTUDIANTE")
            print("11. ELIMINAR MAESTRO")
            print("12. ELIMINAR MATERIA")
            print("13. REGISTRAR CARRERA")
            print("14. REGISTRAR SEMESTRE")
            print("15. MOSTRAR CARRERAS")
            print("16. MOSTRAR SEMESTRES")
            print("17. MOSTRAR GRUPOS")
            print("18. SALIR")

            opcion = input("Ingresa una opcion para continuar -> ")

            if opcion == "1":
                print("+++++++++++++++++ MENU PARA REGISTRO DE ESTUDIANTE++++++++++++++++")
                nombre = input("Ingresa NOMBRE del estudiante -> ")
                apellido = input("Ingresa APELLIDO del estudiante -> ")
                curp = input("Ingresa CURP del estudiante -> ")
                ano = int(input("Ingresa AÑO DE NACIMIENTO del estudiante -> "))
                mes = int(input("Ingresa MES DE NACIMIENTO del estudiante -> "))
                dia = int(input("Ingresa DIA DE NACIMIENTO del estudiante -> "))
                contrasenia=input("Ingresa la contraseña del maestro")
                fecha_nacimiento = datetime(ano, mes, dia)

                numero_control = self.escuela.generar_numero_control()
                print(numero_control)

                estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento,contrasenia=contrasenia)
                self.escuela.registrar_estudiante(estudiante)
                print(f"Estudiante {nombre} registrado exitosamente.")



            elif opcion == "2":
                print("+++++++++++++++++ MENU PARA REGISTRO DE MAESTRO ++++++++++++++++")
                nombre = input("Ingresa NOMBRE del maestro -> ")
                apellido = input("Ingresa APELLIDO del maestro -> ")
                rfc = input("Ingresa RFC del maestro -> ")
                ano_nacimiento = int(input("Ingresa AÑO DE NACIMIENTO del maestro -> "))
                sueldo = float(input("Ingresa el sueldo del maestro: "))
                numero_control_maestro = self.escuela.generar_numero_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
                print(numero_control_maestro)

                maestro = Maestro(numero_control, nombre, apellido, rfc, sueldo)
                self.escuela.registrar_maestro(maestro)
                print(f"Maestro {nombre} registrado exitosamente.")
        
            elif opcion == "3":
                print("+++++++++++++++++ MENU PARA REGISTRO DE MATERIA ++++++++++++++++")
                nombre = input("Ingresa NOMBRE de la materia -> ")
                descripcion = input("Ingresa una DESCRIPCION sobre la materia -> ")
                semestre = input("Ingresa el SEMESTRE de la materia -> ")
                creditos = int(input("Ingresa los CREDITOS de la mteria -> "))
                id = self.escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
                print(id)

                materia = Materia(numero_control, nombre, descripcion, semestre, creditos)
                self.escuela.registrar_materia(materia)
                print(f"Materia {nombre} registrada exitosamente.")


            elif opcion == "4":
                print("\n OPCION PARA REGISTRAR UN NUEVO GRUPO")
                tipo = input("Ingresa el tipo de grupo (A/B)")
                id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo")
                grupo = Grupo()

                self.escuela.registrar_grupo()

            elif opcion == "5":
                pass
            elif opcion == "6":
                self.escuela.listar_estudiante()
                print("TERMINO")
    
            elif opcion == "7":   
                self.escuela.listar_maestros()

            elif opcion == "8":
                self.escuela.listar_materias()

            elif opcion == "9":
                pass
    
            elif opcion == "10":
                numero_control= input("INGRESA NUMERO DE CONTROL")
                self.escuela.eliminar_estudiante(numero_control=numero_control)

            elif opcion == "11":
                n_control=input("Ingresa el numero de control del maestro a eliminar")
                self.escuela.eliminar_materia(n_control)
            elif opcion == "12":
                pass
            elif opcion == "13":
                print("\n OPCION PARA REGISTRAR UNA CARRERA")

                nombre= input("Ingresa el nombre de la carrera -> ")
                carrera = Carrera(nombre=nombre)

            elif opcion == "14":
                print("\n OPCION PARA REGISTRAR SEMESTRE")

                numero = input("Ingresa el numero del semestre")
                id_carrera = input("Ingresa el ID de la carrera")

                semestre = Semestre(numero=numero, id_carrera=id_carrera)

                self.escuela.registrar_semestre(semestre=semestre)
        
            elif opcion == "15":
                self.escuela.lista_carreras()



            elif opcion == "16":
                self.escuela.lista_semestres()

      

            elif opcion == "17":
                self.escuela.lista_grupos()



            elif opcion == "18":
                print("\n HASTA LUEGO")
                break

