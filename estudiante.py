class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante = 0
    cursos = []

    

    def __init__(self, nombre, edad, id_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = id_estudiante
        

    def agregar_curso(self, curso):
        self.cursos.append(curso)

        
    
    def mostrar_informacion(self):
        print(f" ID ESTUDIANTE: {self.id_estudiante}")
        print(f" NOMBRE ESTUDIANTE: {self.nombre}")
        print(f" EDAD: {self.edad}")

        if len(self.cursos) == 0:
            print("NO TIENE CURSOS REGISTRADOS")
            return

        else:
            print("\nCURSOS")
            for curso in self.cursos:
                
                print(f"CURSO: {curso.nombre_curso}")
                print(f"ID: {curso.codigo_curso}")
                print(f"INSTRUCTOR: {curso.instructor}")

                 



