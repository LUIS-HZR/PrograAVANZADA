from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime



while True:

    escuela = Escuela()
    print("-------------------------Mindbox-------------------------------------")
    print("1. REGISTRAR ESTUDIANTE")
    print("2. REGISTRAR MAESTRO")
    print("3. REGISTRAR MATERIA")
    print("4. REGISTRAR GRUPO")
    print("5. REGISTRAR HORARIO")

    opcion = input("Ingresa una opcion para continuar -> ")

    if opcion == "1":
        print("+++++++++++++++++ MENU PARA REGISTRO DE Emaestro++++++++++++++++")
        nombre = input("Ingresa NOMBRE del estudiante -> ")
        apellido = input("Ingresa APELLIDO del estudiante -> ")
        curp = input("Ingresa CURP del estudiante -> ")
        ano = int(input("Ingresa AÑO DE NACIMIENTO del estudiante -> "))
        mes = int(input("Ingresa MES DE NACIMIENTO del estudiante -> "))
        dia = int(input("Ingresa DIA DE NACIMIENTO del estudiante -> "))
        fecha_nacimiento = datetime(ano, mes, dia)
        numero_control = escuela.generar_numero_control()
        print(numero_control)



    elif opcion == "2":
        print("+++++++++++++++++ MENU PARA REGISTRO DE MAESTRO ++++++++++++++++")
        nombre = input("Ingresa NOMBRE del maestro -> ")
        apellido = input("Ingresa APELLIDO del maestro -> ")
        rfc = input("Ingresa RFC del maestro -> ")
        ano_nacimiento = int(input("Ingresa AÑO DE NACIMIENTO del maestro -> "))
        numero_control_maestro = escuela.generar_numero_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
        print(numero_control_maestro)
        
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        print("\n HASTA LUEGO")
        break
