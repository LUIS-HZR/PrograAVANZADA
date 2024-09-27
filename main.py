from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia

escuela = Escuela()

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
    print("9. MOSTRAR GRUPOS")
    print("10. ELIMINAR ESTUDIANTE")
    print("11. ELIMINAR MAESTRO")
    print("12. ELIMINAR MATERIA")
    print("13. SALIR")

    opcion = input("Ingresa una opcion para continuar -> ")

    if opcion == "1":
        print("+++++++++++++++++ MENU PARA REGISTRO DE ESTUDIANTE++++++++++++++++")
        nombre = input("Ingresa NOMBRE del estudiante -> ")
        apellido = input("Ingresa APELLIDO del estudiante -> ")
        curp = input("Ingresa CURP del estudiante -> ")
        ano = int(input("Ingresa AÑO DE NACIMIENTO del estudiante -> "))
        mes = int(input("Ingresa MES DE NACIMIENTO del estudiante -> "))
        dia = int(input("Ingresa DIA DE NACIMIENTO del estudiante -> "))
        fecha_nacimiento = datetime(ano, mes, dia)

        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante)
        print(f"Estudiante {nombre} registrado exitosamente.")
        numero_control = escuela.generar_numero_control()
        print(numero_control)



    elif opcion == "2":
        print("+++++++++++++++++ MENU PARA REGISTRO DE MAESTRO ++++++++++++++++")
        nombre = input("Ingresa NOMBRE del maestro -> ")
        apellido = input("Ingresa APELLIDO del maestro -> ")
        rfc = input("Ingresa RFC del maestro -> ")
        ano_nacimiento = int(input("Ingresa AÑO DE NACIMIENTO del maestro -> "))
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        maestro = Maestro(numero_control, nombre, apellido, rfc, sueldo)
        escuela.registrar_maestro(maestro)
        print(f"Maestro {nombre} registrado exitosamente.")
        numero_control_maestro = escuela.generar_numero_control_maestro(nombre=nombre, rfc=rfc, ano_nacimiento=ano_nacimiento)
        print(numero_control_maestro)

        
    elif opcion == "3":
        print("+++++++++++++++++ MENU PARA REGISTRO DE MATERIA ++++++++++++++++")
        nombre = input("Ingresa NOMBRE de la materia -> ")
        descripcion = input("Ingresa una DESCRIPCION sobre la materia -> ")
        semestre = input("Ingresa el SEMESTRE de la materia -> ")
        creditos = int(input("Ingresa los CREDITOS de la mteria -> "))
        id = escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        materia = Materia(numero_control, nombre, descripcion, semestre, creditos)
        escuela.registrar_materia(materia)
        print(f"Materia {nombre} registrada exitosamente.")
        print(id)



    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        escuela.listar_estudiante()
        print("TERMINO")
    
    elif opcion == "7":
        escuela.listar_maestros()
        print("TERMINO")

    elif opcion == "8":
        escuela.listar_materias()
        print("TERMINO")

    elif opcion == "9":
        pass
    
    elif opcion == "10":
        numero_control= input("INGRESA NUMERO DE CONTROL")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        n_control=input("Ingresa el numero de control del maestro a eliminar")
        escuela.eliminar_materia(n_control)
        
    elif opcion == "12":
        pass
    elif opcion == "13":
        print("\n HASTA LUEGO")
        break
