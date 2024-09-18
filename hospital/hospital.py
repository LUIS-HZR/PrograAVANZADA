from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta

class Hospital:
    pacientes: List[Paciente]=[]
    pacientes_menores: List[Paciente]= []
    pacientes_mayores: List[Paciente]= []
    medicos: List[Medico]=[]
    consultas: List[Consulta]=[]

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("*** No se puede registrar la consulta, no existe el médico o el paciente ***")
            return
        
        print(" -> Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self, paciente):
        print("*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()

    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True
            
    def lista_pacientes_menores(self,pacientes):
        for paciente in self.pacientes:
            if paciente.ano_nacimiento > 2006:
                self.pacientes_menores.append(pacientes)
                paciente.mostrar_informacion()
                print("\n++++++++++++++++")
                
        if len(self.pacientes_menores) == 0:
                    print("NO HAY PACIENTES MENORES DE EDAD")
        else:
            return

    def lista_pacientes_mayores(self, pacientes):
        for paciente in self.pacientes:
            if paciente.ano_nacimiento < 2006:
                self.pacientes_mayores.append(pacientes)
                paciente.mostrar_informacion()
                print("\n++++++++++++++++")
                
        if len(self.pacientes_mayores) == 0:
                    print("NO HAY PACIENTES MAYORES DE EDAD")
        else:
            return
    

    def eliminar_paciente(self, id_paciente_eliminar):
        for paciente in self.pacientes:
             if paciente.id == id_paciente_eliminar:
                  self.pacientes.remove(paciente)
                  print("\n SE ELIMINO EL PACIENTE CON ID: ", id_paciente_eliminar)
                  break
        
        
    def eliminar_medico(self, id_medico_eliminar):
        for paciente in self.pacientes:
             if paciente.id == id_medico_eliminar:
                  self.pacientes.remove(paciente)
                  print("\n SE ELIMINO EL MEDICO CON ID: ", id_medico_eliminar)
                  break   

    def mostrar_id(self):
         for paciente in self.pacientes:
             print(f"{paciente.nombre}")
             print(f"\n{paciente.id}")
    def mostrar_med_id(self):
         for medico in self.medicos:
             print(f"{medico.id}")



