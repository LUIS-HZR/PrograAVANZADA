from circulo import Circulo

circulo_uno = Circulo(3)
circulo_dos = Circulo(5)
circulo_tres = Circulo(4)


print("CIRCULO 1 DE RADIO = ", circulo_uno.radio)
print("\n AREA CIRCULO 1: ")
Circulo.calcular_area(circulo_uno)
print("\n PERIMETRO CIRCULO 1: ")
Circulo.calcular_perimetro(circulo_uno)
print("----------------------------------------------------------------------")
print("CIRCULO 2 DE RADIO = ", circulo_dos.radio)
print("\n AREA CIRCULO 2: ")
Circulo.calcular_area(circulo_dos)
print("\n PERIMETRO CIRCULO 2: ")
Circulo.calcular_perimetro(circulo_dos)
print("----------------------------------------------------------------------")
print("CIRCULO 3 DE RADIO = ", circulo_tres.radio)
print("\n AREA CIRCULO 3: ")
Circulo.calcular_area(circulo_tres)
print("\n PERIMETRO CIRCULO 3: ")
Circulo.calcular_perimetro(circulo_tres)
print("\n")


