from datetime import datetime
from random import randint

class Animal:
    tipo:str
    id_animal=str
    fecha_llegada:datetime
    enfermedades: str
    tipo_alimentacion: str
    fecha_nacimiento:datetime
    peso: float
    frecuencia_alimentacion: str
    vacunas: bool

    def __init__(self, tipo:str, id_animal: str, fecha_llegada:datetime, enfermedades:str, tipo_alimentacion: str, fecha_nacimiento:datetime, peso:int, frecuencia_alimentacion: str, vacunas:bool):
        self.tipo=tipo
        self.id_animal = id_animal
        self.fecha_llegada=fecha_llegada
        self.enfermedades=enfermedades
        self.tipo_alimentacion=tipo_alimentacion
        self.fecha_nacimiento=fecha_nacimiento
        self.peso=peso
        self.frecuencia_alimentacion=frecuencia_alimentacion
        self.vacunas=vacunas


    def mostrar_info_animales(self):
        info=f"Tipo:{self.tipo},ID:{self.id_animal} Fecha de llegada:{self.fecha_llegada}, Enfermedades:{self.enfermedades}, Tipo de alimentacion:{self.tipo_alimentacion}, Fecha de nacimiento:{self.fecha_nacimiento}, Peso:{self.peso}, Frecuecnia de alimentacion:{self.frecuencia_alimentacion}, Vacunas:{self.vacunas}"
        return info
    

    
    def modificar_animal(self, id_animal:str):
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

            animal_nuevo=Animal(tipo=tipo,id_animal=id_animal,fecha_llegada=fecha_llegada, enfermedades=enfermedades, tipo_alimentacion=tipo_alimentacion, fecha_nacimiento=fecha_de_nacimiento, peso=peso, frecuencia_alimentacion=frecuencia_alimentacion, vacunas=vacunas)
            return animal_nuevo
        

        
