from datetime import datetime
from zoologico.zoologico import Zoologico
from empleados.empleados import Empleado
from guias.guia import Guia
from veterinarios.veterinario import Veterinario
from mantenimiento.mantenimiento import Mantenimiento
from visitantes.visitantes import Visitante
from zoologico.zoologico import Zoologico
from visitas.visita import Visita
from reparaciones.reparaciones import Reparaciones
from animales.animales import Animal

class Menu:
    zoologico = Zoologico()
    
    
        
    def mostrar_menu(self):
        while True:
            print("** MENU PRINCIPAL **")
            print("1.- Registrar empleado guia")
            print("2.- Registrar empleado veterinario")
            print("3.- Registrar empleado mantenimiento")
            print("4.- Registrar visitante")
            print("5.- Registrar visita")
            print("6.- Registrar animal")
            print("7.- Registrar mantenimientos")
            
            print("8.- Modificar datos empleado guia")
            print("9.- Modificar datos empleado veterinario")
            print("10.- Modificar datos empleado mantenimiento")
            print("11.- Modificar datos visitante")
            print("12.- Modificar datos animal")
            
            print("13.- Eliminar empleado guia")
            print("14.- Eliminar empleado veterinario")
            print("15.- Eliminar empleado mantenimiento")
            print("16.- Eliminar visitante")
            print("17.- Eliminar animal")
            
            print("18.- Mostrar empleados")
            print("19.- Mostrar visitantes")
            print("20.- Mostrar visitas")
            print("21.- Mostrar animal")
            print("22.- Mostrar mantenimientos")
            
            print("23.- Agregar visitante a visita")
            print("24.- Salir")
            opcion = input("\nIngrese la opcion de lo que desea realizar: ")

            if opcion == "1":
                print("\nINGRESE DATOS DEL GUIA")  
                nombre = str(input("Ingrese el nombre del empleado: "))
                apellido = str(input("Ingrese el apellido del empleado: "))
                curp = str(input("Ingrese la curp del empleado: "))
                dia = int(input("Ingrese el dia de nacimiento: "))
                mes = int(input("Ingrese el mes de nacimeinto: "))
                anio = int(input("Ingrese el año de nacimiento: "))
                dia_ingreso = int(input("Ingrese el dia de ingreso al empleo: "))
                mes_ingreso = int(input("Ingrese el mes de ingreso al empleo: "))
                anio_ingreso = int(input("Ingrese el año de ingreso al empleo: "))
                rfc = str(input("Ingrese el rfc del empleado: "))
                salario = float(input("Ingrese el salario del empleado: "))
                id = self.zoologico.generar_id_empleado(apellido=apellido,rfc=rfc)
                horario = str(input("Ingrese el horario de trabajo(hrs trabajadas al dia): "))
                
                fecha_nacimiento = datetime(anio, mes, dia)
                fecha_ingreso = datetime(anio_ingreso,mes_ingreso,dia_ingreso)
                guia = Guia(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario,horario=horario)
                self.zoologico.registrar_guia(guia=guia)
                
            elif opcion == "2":
                print("\nINGRESE DATOS DEL VETERINARIO")  
                nombre = str(input("Ingrese el nombre del empleado: "))
                apellido = str(input("Ingrese el apellido del empleado: "))
                curp = str(input("Ingrese la curp del empleado: "))
                dia = int(input("Ingrese el dia de nacimiento: "))
                mes = int(input("Ingrese el mes de nacimeinto: "))
                anio = int(input("Ingrese el año de nacimiento: "))
                dia_ingreso = int(input("Ingrese el dia de ingreso al empleo: "))
                mes_ingreso = int(input("Ingrese el mes de ingreso al empleo: "))
                anio_ingreso = int(input("Ingrese el año de ingreso al empleo: "))
                rfc = str(input("Ingrese el rfc del empleado: "))
                salario = float(input("Ingrese el salario del empleado: "))
                id = self.zoologico.generar_id_empleado(apellido=apellido,rfc=rfc)
                horario = str(input("Ingrese el horario de trabajo(hrs trabajadas al dia): "))
                
                fecha_nacimiento = datetime(anio, mes, dia)
                fecha_ingreso = datetime(anio_ingreso,mes_ingreso,dia_ingreso)
                veterinario = Veterinario(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario,horario=horario)
                self.zoologico.registrar_veterinario(veterinario=veterinario)
                
            elif opcion == "3":
                print("\nINGRESE DATOS DEL EMPLEADO MANTENIMIENTO")  
                nombre = str(input("Ingrese el nombre del empleado: "))
                apellido = str(input("Ingrese el apellido del empleado: "))
                curp = str(input("Ingrese la curp del empleado: "))
                dia = int(input("Ingrese el dia de nacimiento: "))
                mes = int(input("Ingrese el mes de nacimeinto: "))
                anio = int(input("Ingrese el año de nacimiento: "))
                dia_ingreso = int(input("Ingrese el dia de ingreso al empleo: "))
                mes_ingreso = int(input("Ingrese el mes de ingreso al empleo: "))
                anio_ingreso = int(input("Ingrese el año de ingreso al empleo: "))
                rfc = str(input("Ingrese el rfc del empleado: "))
                salario = float(input("Ingrese el salario del empleado: "))
                id = self.zoologico.generar_id_empleado(apellido=apellido,rfc=rfc)
                horario = str(input("Ingrese el horario de trabajo(hrs trabajadas al dia): "))
                
                fecha_nacimiento = datetime(anio, mes, dia)
                fecha_ingreso = datetime(anio_ingreso,mes_ingreso,dia_ingreso)
                empleado_mantenimiento = Mantenimiento(nombre=nombre,apellido=apellido,id=id,curp=curp,fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_ingreso,rfc=rfc,salario=salario,horario= horario)
                self.zoologico.registrar_empleado_mantenimiento(empleado_mantenimiento=empleado_mantenimiento)
                
            elif opcion == "4":
                print("\nINGRESE DATOS DEL VISITANTE")
                nombre = input("Ingresa NOMBRE(S) del visitante -> ")
                apellido = input("Ingresa PRIMER APELLIDO del visitante -> ")
                curp = input("Ingresa CURP del visitante -> ")
                ano = int(input("Ingresa AÑO DE NACIMIENTO del visitante -> "))
                mes = int(input("Ingresa MES DE NACIMIENTO del visitante -> "))
                dia = int(input("Ingresa DIA DE NACIMIENTO del visitante -> "))
                fecha_nacimiento = datetime(ano, mes, dia)
                ano_registro = int(input("Ingresa AÑO DE REGISTRO del visitante -> "))
                mes_registro = int(input("Ingresa MES DE REGISTRO del visitante -> "))
                dia_registro = int(input("Ingresa DIA DE REGISTRO del visitante -> "))
                fecha_de_registro = datetime(ano_registro, mes_registro, dia_registro)
                id = self.zoologico.generar_id_visitantes(apellido=apellido)
                print(id)

                visitante = Visitante(nombre=nombre, apellido=apellido, curp=curp, id=id, fecha_nacimiento=fecha_nacimiento, fecha_de_registro= fecha_de_registro, ano=ano)
                
                #fecha_de_visitas=self.zoologico.listar_visita()
                #numero_visitas=self.zoologico.generar_fecha_de_visita(visita=visita)

                if ano < 2006:
                    adulto = visitante
                    self.zoologico.registrar_visitante_adulto(adulto= adulto)
                else:
                    nino = visitante
                    self.zoologico.registrar_visitante_nino(Nino=nino)

            elif opcion == "5":

                print("\nINGRESE DATOS DE LA VISITA")
                dia_v=int(input("Ingrese dia de la visita: "))
                mes_v=int(input("Ingrese mes de la visita: "))
                ano_v=int(input("Ingrese año de la visita: "))
                fecha_visita = datetime(ano_v, mes_v, dia_v)
                id_visitante = input("Ingresa el id del visitante: ")
                guia_a_cargo=input("Ingrese el id del guia a cargo: ")
                id=self.zoologico.generar_id_visita()
                print(id)
                
                visita=Visita(fecha_visita=fecha_visita, guia_a_cargo=guia_a_cargo,id_visitante=id_visitante, id=id )

                self.zoologico.registrar_visita(visita)
                    
            elif opcion == "6":
                print("\nREGISTRE UN ANIMAL")
                tipo=str(input("Ingrese el tipo de animal: "))
                dia_ingreso=int(input("Ingrese del dia de llegada: "))
                mes_ingreso=int(input("Ingrese del mes de llegada: "))
                anio_ingreso=int(input("Ingrese del año de llegada: "))
                enfermedades=str(input("Ingrese las enfermedades del animal: "))
                tipo_alimentacion=str(input("Ingrese el tipo de alimentacion: "))
                dia=int(input("Ingrese el dia de nacimiento: "))
                mes=int(input("Ingrese el mes de nacimiento: "))
                anio=int(input("Ingrese el año de nacimiento: "))
                peso=float(input("Ingrese el peso del animal: "))
                frecuencia_alimentacion=str(input("Ingresa la frecuencia de alimentacion: "))
                vacunas=bool(input("El animal tiene vacvunas: "))

                fecha_llegada=datetime(anio_ingreso, mes_ingreso, dia_ingreso)
                fecha_de_nacimiento=datetime(anio, mes, dia)
                id_animal = self.zoologico.generar_id_animal()

                animal=Animal(tipo=tipo,id_animal = id_animal,fecha_llegada=fecha_llegada, enfermedades=enfermedades, tipo_alimentacion=tipo_alimentacion, fecha_nacimiento=fecha_de_nacimiento, peso=peso, frecuencia_alimentacion=frecuencia_alimentacion, vacunas=vacunas)
                self.zoologico.registrar_animal(animal)

            elif opcion == "7":
                print("\nREGISTRE ALGUN MANTENIMIENTO\n")
                empleado_encargado = input("Ingrese el ID de un empleado de mantenimiento: ")
                proceso_realizado = input("Ingrese el proceso que se llevo a cabo: ")
                observaciones = input("Ingrese algunas observaciones que se tienen que tomar en cuenta en el mantenimiento: ")
                id_animal = input("Ingrese el ID de un animal: ")
                dia_proceso = int(input("Ingrese el dia en el que se realizo el mantenimiento: "))
                mes_proceso = int(input("Ingrese el mes en el que se realizo el mantenimiento: "))
                anio_proceso = int(input("Ingrese el año en el que se realizo el mantenimiento: "))
                fecha_proceso = datetime(anio_proceso, mes_proceso, dia_proceso)
                
                mantenimiento = Reparaciones(empleado_encargado= empleado_encargado,proceso_realizado=proceso_realizado,observaciones=observaciones,id_animal=id_animal,fecha_proceso=fecha_proceso)
                self.zoologico.registrar_mantenimiento(mantenimiento)

            elif opcion == "8":
                print("\nMODIFICAR GUIA\n")
                id_empleado = input("Ingrese el ID del empleado que desea modificar la informacion: ")
                self.zoologico.modificar_datos_guia(id_empleado= id_empleado)
                
            elif opcion == "9":
                print("\nMODIFICAR GUIA\n")
                id_empleado = input("Ingrese el ID del empleado que desea modificar la informacion: ")
                self.zoologico.modificar_datos_veterinario(id_empleado= id_empleado)
                
            elif opcion == "10":
                print("\nMODIFICAR GUIA\n")
                id_empleado = input("Ingrese el ID del empleado que desea modificar la informacion: ")
                self.zoologico.modificar_datos_empleado_mantenimiento(id_empleado= id_empleado)
            
            elif opcion == "11": #MODIFICAR DATOS DE VISITANTE
                 print("\nMODIFICAR VISITANTE\n")
                 id_visitante = input("Ingrese el ID del visitante que desea modificar la informacion: ")
                 self.zoologico.modificar_datos_visitante(id_visitante= id_visitante)

            elif opcion == "12":
                print("MODIFICAR ANIMAL")
                id_animal=input("Ingrese el ID del animal: ")
                self.zoologico.modificar_datos_animal(id_animal=id_animal)

            elif opcion == "13":
                print("\nELIMINE UN GUIA\n")
                id_empleado = str(input("Coloque el ID del empleado que desea eliminar: "))
                self.zoologico.eliminar_guia(id_empleado= id_empleado)
                
            elif opcion == "14":
                print("\nELIMINE UN VETERINARIO\n")
                id_empleado = str(input("Coloque el ID del empleado que desea eliminar: "))
                self.zoologico.eliminar_veterinario(id_empleado= id_empleado)
                
            elif opcion == "15":
                print("\nELIMINE UN EMPLEADO DE MANTENIMIENTO\n")
                id_empleado = str(input("Coloque el ID del empleado que desea eliminar: "))
                self.zoologico.eliminar_empleado_mantenimiento(id_empleado= id_empleado)
            
            elif opcion == "16":
                print("\nELIMINE UN VISITANTE\n")
                id = str(input("Coloque el ID del VISITANTE que desea eliminar: "))
                self.zoologico.eliminar_visitante(id=id)

            elif opcion == "17":
                print("ELIMINAR UN ANIMAL")
                id_animal=str(input("Ingrese el ID del animal a eliminar: "))
                self.zoologico.eliminar_animal(id_animal=id_animal)                

            elif opcion == "18":
                self.zoologico.mostrar_empleados()
            
            elif opcion == "19":
                self.zoologico.mostrar_visitantes()

            elif opcion == "20": #MOSTRAR VISITAS
                self.zoologico.mostrar_visitas()


            elif opcion == "21":
                self.zoologico.mostrar_animal()

            elif opcion == "22":
                self.zoologico.mostrar_mantenimiento()
            
            elif opcion == "23":
                id_v_a= input("Ingresa id del visitante")
                id_vt= input("Ingresa el id de la visita")

                self.zoologico.registrar_visitante_a_visita(id_v_a=id_v_a, id_vt=id_vt)

            elif opcion == "24":
                print("Hasta luego\n")
                break