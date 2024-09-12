import math

class Circulo:
    radio = 0

    def __init__(self,radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * pow(self.radio,2)
        print(area)

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        print(perimetro)

