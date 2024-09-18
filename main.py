from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()

paciente_uno = Paciente("Juan", 2004, 76, 1.78, "Av. Madero")
paciente_dos = Paciente("Jesus", 2008, 73, 1.68, "Av. Periodismo")
paciente_tres = Paciente("Jonathan", 2009, 79, 1.80, "Av. Madero")
paciente_cuatro = Paciente("Valeria", 2003, 56, 1.60, "Lagos de moreno")
paciente_cinco = Paciente("Jorge", 2004, 56, 1.68, "Lagos de moreno")

medico_uno = Medico("Chuyin", 2004, "jjsjsjsdjd", "Acueducto")
medico_dos = Medico("Alberto", 1978, "ALB4817BNDDDF", "Av. Periodismo")
medico_tres = Medico("Carlos", 1999, "ALB4827BNDJDF", "Av. Periodismo")

hospital.registrar_paciente(paciente=paciente_uno)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)
hospital.registrar_paciente(paciente=paciente_cuatro)
hospital.registrar_paciente(paciente=paciente_cinco)

hospital.registrar_medico(medico=medico_uno)
hospital.registrar_medico(medico=medico_dos)
hospital.registrar_medico(medico=medico_tres)

while True:
    print("_______________ BIENVENIDO A SISTEMA ________________________")
    print("  + OPCIONES: ")
    print("        -> MOSTRAR PACIENTES (1)")
    print("        -> ELIMINAR PACIENTE (2)")
    print("        -> ELIMINAR MEDICO (3)")
    print("        -> SALIR (3)")
    opcion = input("\nINGRESA LA OPCION: ")

    if opcion == "1":
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
    elif opcion == "2":
        hospital.mostrar_id()
        id_paciente_eliminar = int(input("\n INGRESE EL ID DEL PACIENTE --> "))
        hospital.eliminar_paciente(id_paciente_eliminar)
        print("\n PACIENTE ELIMINADO")
    elif opcion == "3":
        hospital.mostrar_med_id()
        id_medico_eliminar = int(input("\n INGRESE EL ID DEL PACIENTE --> "))
        hospital.eliminar_paciente(id_medico_eliminar)
        print("\n PACIENTE ELIMINADO")

    else:        
        break


# hospital.registrar_consulta(id_paciente=2, id_medico=3)
# hospital.mostrar_pacientes(paciente=[])
