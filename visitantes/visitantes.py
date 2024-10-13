from datetime import datetime


class Visitante():
    nombre: str
    fecha_nacimiento: datetime
    numero_visitas: int
    apellido1: str
    apellido2: str
    curp: str
    fecha_de_registro: datetime
    fecha_de_visitas: datetime
    cant_adultos: int


    def __init__(self, fecha_de_visitas, cant_adultos, nombre: str, fecha_nacimiento: datetime, numero_visitas: int,apellido1: str, apellido2: str,curp: str, fecha_de_registro: datetime):
        self.fecha_de_visitas=fecha_de_visitas
        self.cant_adultos=cant_adultos
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.numero_visitas=numero_visitas
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.curp= curp
        self.fecha_de_registro=fecha_de_registro

    
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre}{self.apellido1}{self.apellido2}"
        info = f"Nombre completo: {nombre_completo}, Curp: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento}, Fecha de registro: {self.fecha_de_registro} Numero de visitas: {self.numero_visitas}"
        return info



        #print("+++++++++++++++++ MENU PARA REGISTRO DE VISITANTE++++++++++++++++")
                #nombre = input("Ingresa NOMBRE(S) del visitante -> ")
                #apellido1 = input("Ingresa PRIMER APELLIDO del visitante -> ")
                #apellido2 = input("Ingresa SEGUNDO APELLIDO del visitante -> ")
                ##curp = input("Ingresa CURP del visitante -> ")
                #ano = int(input("Ingresa AÑO DE NACIMIENTO del visitante -> "))
                #mes = int(input("Ingresa MES DE NACIMIENTO del visitante -> "))
                #dia = int(input("Ingresa DIA DE NACIMIENTO del visitante -> "))
                #fecha_nacimiento = datetime(ano, mes, dia)

                #visitante=Visitante(nombre=nombre, apellido1=apellido1, apellido2=apellido2, curp=curp, ano=ano, mes=mes, dia=dia)
                #self.zoologico.registrar_visitante(visitante)
    
        