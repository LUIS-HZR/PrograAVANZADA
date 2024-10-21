from datetime import datetime
from usuario.utils.roles import Rol
from usuario.usuario import Usuario


class Visitante(Usuario):
    fecha_de_registro: datetime
    #lista_visita: str
    #fecha_de_visitas:datetime
    numero_visitas: int


    def __init__(self, id: str, nombre: str, fecha_nacimiento: datetime,apellido: str,curp: str, fecha_de_registro: datetime, ano: int):
        
        if 2024 - ano > 18:
            #ADULTO
            super().__init__(nombre=nombre, apellido=apellido, id=id, curp=curp, fecha_nacimiento=fecha_nacimiento,rol=Rol.ADULTO)
            self.fecha_de_registro = fecha_de_registro

        else:
            #NIÑO 
            super().__init__(nombre=nombre, apellido=apellido, id=id, curp=curp, fecha_nacimiento=fecha_nacimiento,rol=Rol.NINO)
            self.fecha_de_registro = fecha_de_registro



        #self.lista_visitas=lista_visitas
        
         #self.numero_visitas=numero_visitas
    
    
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"- Nombre completo: {nombre_completo}\n- ID: {self.id}\n-Curp: {self.curp}\n- Fecha de nacimiento: {self.fecha_nacimiento}\n- Fecha de registro: {self.fecha_de_registro}\n- Persona: {self.rol.value}\n"
        return info
    
    def sumar_numero_visitas(self,numero_visitas):
        numero_visitas += 1
        return numero_visitas
    
    def modificar_info_visitante(self, id_visitante: str):
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
        
        visitante_nuevo = Visitante(nombre=nombre, apellido=apellido, curp=curp, id=id, fecha_nacimiento=fecha_nacimiento, fecha_de_registro= fecha_de_registro, ano=ano)
        return visitante_nuevo
