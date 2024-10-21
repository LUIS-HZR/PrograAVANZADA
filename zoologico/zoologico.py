from typing import List
from random import randint
from visitantes.visitantes import Visitante
from empleados.empleados import Empleado
from veterinarios.veterinario import Veterinario
from guias.guia import Guia
from mantenimiento.mantenimiento import Mantenimiento
from animales.animales import Animal
from visitas.visita import Visita
from reparaciones.reparaciones import Reparaciones

class Zoologico():
    lista_empleados: List[Empleado] = []
    lista_guias: List[Guia]= []
    lista_veterinarios: List[Veterinario] = []
    lista_empleado_mantenimiento: List[Mantenimiento] = []
    lista_visitantes: List[Visitante] = []
    lista_visitantes_adulto: List[Visitante] = []
    lista_visitantes_nino: List[Visitante] = []
    lista_animales: List[Animal] = []
    lista_visita: List[Visita]=[]
    lista_mantenimientos: List[Mantenimiento] = []
    
    
    def registrar_visitante(self, visitante: Visitante):
        self.lista_visitantes.append(visitante)
        print("\nSe registro correctamente\n")

    def registrar_guia(self, guia: Guia):
        self.lista_empleados.append(guia)
        self.lista_guias.append(guia)
        print("\nSe registro correctamente")
        print("ID generado: ",guia.id, "\n")

    def registrar_veterinario(self, veterinario: Veterinario):
        self.lista_empleados.append(veterinario)
        self.lista_veterinarios.append(veterinario)
        print("\nSe registro correctamente")
        print("ID generado: ",veterinario.id, "\n")

    def registrar_empleado_mantenimiento(self, empleado_mantenimiento: Mantenimiento):
        self.lista_empleados.append(empleado_mantenimiento)
        self.lista_empleado_mantenimiento.append(empleado_mantenimiento)
        print("\nSe registro correctamente")
        print("ID generado: ",empleado_mantenimiento.id, "\n")
    
    def registrar_visitante_adulto(self, adulto: Visitante):
        self.lista_visitantes.append(adulto)
        self.lista_visitantes_adulto.append(adulto)
        print("\nSe registro correctamente\n")

    def registrar_visitante_nino(self, Nino: Visitante):
        self.lista_visitantes.append(Nino)
        self.lista_visitantes_nino.append(Nino)
        print("\nSe registro correctamente\n")

    def registrar_visita(self, visita:Visita):
        self.lista_visita.append(visita)
        print("\nSe registro correctamente\n")

    def registrar_animal(self, animal:Animal):
        self.lista_animales.append(animal)
        print("\nSe registro correctamente\n")
        print("ID generado: ",animal.id_animal, "\n")

    def registrar_mantenimiento(self, mantenimiento: Reparaciones):
        for id_mantenimiento in self.lista_empleado_mantenimiento:
            for id_Animal in self.lista_animales:
                if id_mantenimiento.id == mantenimiento.empleado_encargado and id_Animal.id_animal == mantenimiento.id_animal:
                        self.lista_mantenimientos.append(mantenimiento)
                        print("\nSe registro correctamente\n")     
                        return   
        print("\nNo existe el empleado de mantenimiento o el animal")

        
    def modificar_datos_guia(self, id_empleado: str):
        for empleado in self.lista_empleados:
            for empleado in self.lista_guias:
                if empleado.id == id_empleado:
                    self.lista_empleados.remove(empleado)
                    self.lista_guias.remove(empleado)
                    guia_nuevo = empleado.modificar_info(id_empleado = id_empleado)
                    self.lista_empleados.append(guia_nuevo)
                    self.lista_guias.append(guia_nuevo)
                    print("\nSe modifico la informacion correctamente\n")
                
    def modificar_datos_veterinario(self, id_empleado: str):
        for empleado in self.lista_empleados:
            for empleado in self.lista_veterinarios:
                if empleado.id == id_empleado:
                    self.lista_empleados.remove(empleado)
                    self.lista_veterinarios.remove(empleado)
                    veterinario_nuevo = empleado.modificar_info(id_empleado = id_empleado)
                    self.lista_empleados.append(veterinario_nuevo)
                    self.lista_veterinarios.append(veterinario_nuevo)
                    print("\nSe modifico la informacion correctamente\n")
                
    def modificar_datos_empleado_mantenimiento(self, id_empleado: str):
        for empleado in self.lista_empleados:
            for empleado in self.lista_empleado_mantenimiento:
                if empleado.id == id_empleado:
                    self.lista_empleados.remove(empleado)
                    self.lista_empleado_mantenimiento.remove(empleado)
                    empleado_mantenimiento_nuevo = empleado.modificar_info(id_empleado = id_empleado)
                    self.lista_empleados.append(empleado_mantenimiento_nuevo)
                    self.lista_empleado_mantenimiento.append(empleado_mantenimiento_nuevo)
                    print("\nSe modifico la informacion correctamente\n")

    def modificar_datos_visitante(self,id_visitante: str):
        for visitantes in self.lista_visitantes:
            if visitantes.id == id_visitante:
                self.lista_visitantes.remove(visitantes)
                visitante_nuevo = visitantes.modificar_info(id_empleado = id_visitante)
                self.lista_visitantes.append(visitante_nuevo)
                print("\nSe modifico la informacion correctamente\n")
    
    def modificar_datos_animal(self, id_animal:str):
        for animal in self.lista_animales:
            if animal.id==id_animal:
                self.lista_animales.remove(animal)
                animal_nuevo=animal.modificar_animal(id_animal=id_animal)
                self.lista_animales.append(animal_nuevo)
                print("Se modificaron los datos")
    
    def eliminar_guia(self, id_empleado: str):
        for empleado in self.lista_empleados:
            if empleado.id == id_empleado:
                self.lista_guias.remove(empleado)
                self.lista_empleados.remove(empleado)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id_empleado)
        
    def eliminar_veterinario(self, id_empleado: str):
        for empleado in self.lista_empleados:
            if empleado.id == id_empleado:
                self.lista_veterinarios.remove(empleado)
                self.lista_empleados.remove(empleado)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id_empleado)
        
    def eliminar_empleado_mantenimiento(self, id_empleado: str):
        for empleado in self.lista_empleados:
            if empleado.id == id_empleado:
                self.lista_empleado_mantenimiento.remove(empleado)
                self.lista_empleados.remove(empleado)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id_empleado)
            
    def eliminar_visitante(self, id: str):
        for visitante in self.lista_visitantes:
            if visitante.id == id:
                self.lista_visitantes.remove(visitante)
                print("\nSe eliminó correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id)

    def eliminar_animal(self, id_animal:str):
        for animal in self.lista_animales:
            if animal.id_animal==id_animal:
                self.lista_animales.remove(animal)
                print("Se elimino el animal")
                return
        print("No se encontro el animal con el ID dado")
        
    def mostrar_empleados(self):
        print("\n** EMPLEADOS **\n")
        for empleado in self.lista_empleados:
            print(empleado.mostrar_info_empleado())
       
    def mostrar_visitantes(self):
        print("\n** VISITANTES **\n")
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())
        
    def mostrar_animal(self):
        print("ANIMALES")
        for animal in self.lista_animales:
            print(animal.mostrar_info_animales())

    def mostrar_visitas(self):
        print("\n** VISITAS **\n")
        for visita in self.lista_visita:
            print(visita.mostrar_visita())
    
    def mostrar_mantenimiento(self):
        print("\n** MANTENIMIENTOS **\n")
        for mantenimiento in self.lista_mantenimientos:
            print(mantenimiento.mostrar_info_mantenimiento())
        
    def generar_id_empleado(self,apellido: str,rfc: str ):
        primeros_digitos = apellido[0:2].upper()
        ultimos_digitos = rfc[0:-2].upper()
        id = f"{primeros_digitos}-{ultimos_digitos}-{randint(1,10000)}"
        return id
    
    def generar_id_visitantes(self, apellido:str):
        primer_letra = apellido[:2].upper()
        aleatorio = randint(200, 6000)
        id_visitante = f"M-{primer_letra}{aleatorio}"
        
        return id_visitante
    
    def generar_id_visita(self ):
        
        aleatorio = randint(200, 6000)
        id_visita = f"V-{aleatorio}"
        
        return id_visita
    
    def generar_id_animal(self):
         aleatorio=randint(10000,20000)
         id_animal=f"A-{aleatorio}"
         return id_animal

    def registrar_visitante_a_visita(self, id_vt:str, id_v_a:str):
        for visitante in self.lista_visitantes:
            if visitante.id == id_v_a:
                for visita in self.lista_visita:
                    if visita.id == id_vt:
                        self.lista_visita.append(visitante)
                        visita.ingresar_visitantes(visitante=visitante)

                        visitante.sumar_numero_visitas()

                print("\nSe registró correctamente\n")
            return 
        print("\nNo se encontró el empleado con el id: ",id)


    # def listar_visita(self):
    #     for visita in self.lista_visita:
    #         print("FECHA: ")
    #         print(visita.mostrar_visita())

    #         print()

