from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()


while True:
    print("_______________ BIENVENIDO A SISTEMA ________________________")
    print("  + OPCIONES: ")
    print("        -> AGREGAR PACIENTE (1)")
    print("        -> AGREGAR MEDICO (2)")
    print("        -> ELIMINAR PACIENTE (3)")
    print("        -> ELIMINAR MEDICO (4)")
    print("        -> MOSTRAR PACIENTES (5)")
    print("        -> SALIR (6)")
    opcion = input("\nINGRESA LA OPCION: ")

    if opcion == "1":
        print("INGRESE DATOS PARA REGISTRAR PACIENTE")

        nombre = input("INGRESE EL NOMBRE -> ")
        ano_nacimiento = int(input("INGRESE EL AÑO DE NACIMIENTO -> "))
        peso = int(input("INGRESE EL PESO -> "))
        estatura = int(input("INGRESE LA ESTATURA-> "))
        direccion = input("INGRESE LA DIRECCION-> ")

        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("PACIENTE REGISTRADO CORRECTAMENTE")


    elif opcion == "2":
        print("INGRESE DATOS PARA REGISTRAR MEDICO")

        nombre = input("INGRESE EL NOMBRE -> ")
        ano_nacimiento = int(input("INGRESE EL AÑO DE NACIMIENTO -> "))
        rfc = input("INGRESE EL RFC -> ")
        direccion = input("INGRESE LA DIRECCION-> ")

        medico = Medico(nombre=nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("PACIENTE REGISTRADO CORRECTAMENTE")


    elif opcion == "5":
        print("+ OPCIONES:")
        print("    -> PACIENTES MENORES DE EDAD(1)")
        print("    -> PACIENTES MAYORES DE EDAD(2)")
        opcion2 = input("\n INGRESE LA OPCION 2: ")
        
        if opcion2 == "1":
            hospital.lista_pacientes_menores(pacientes=[])
            print("CARGA COMPLETADA")
            print("\n")

            
        elif opcion2 == "2":
            hospital.lista_pacientes_mayores(pacientes=[])
            print("CARGA COMPLETADA")
            print("\n")

    elif opcion == "3":
        hospital.mostrar_id()
        id_paciente_eliminar = int(input("\n INGRESE EL ID DEL PACIENTE --> "))
        hospital.eliminar_paciente(id_paciente_eliminar)
        print("\n PACIENTE ELIMINADO")
    elif opcion == "4":
        hospital.mostrar_med_id()
        id_medico_eliminar = int(input("\n INGRESE EL ID DEL MEDICO --> "))
        hospital.eliminar_paciente(id_medico_eliminar)
        print("\n MEDICO ELIMINADO")

    else:        
        break


# hospital.registrar_consulta(id_paciente=2, id_medico=3)
# hospital.mostrar_pacientes(paciente=[])
