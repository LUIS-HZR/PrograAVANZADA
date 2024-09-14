from curso import Curso
from estudiante import Estudiante 

curso_uno = Curso("MECANISMOS", "Fernando Saldaña", 456744)
curso_dos = Curso("DINAMICA DE SISTEMAS", "Arturo Suarez", 456866)
curso_tres = Curso("VIBRACIONES MECANICAS", "Daniel Molinero", 456988)

estudiante_uno = Estudiante("Valeria", 22, 1234)
estudiante_dos = Estudiante("LUIS", 20, 4321)

estudiante_uno.agregar_curso(curso_dos)
estudiante_dos.agregar_curso(curso_uno)

estudiante_uno.mostrar_informacion()
print("----------------------------------------------")
estudiante_dos.mostrar_informacion()
