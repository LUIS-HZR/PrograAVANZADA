class Curso:
    nombre_curso = ""
    instructor = ""
    codigo_curso = 0

    def __init__(self, nombre_curso, instructor, codigo_curso):
        self.nombre_curso = nombre_curso
        self.instructor = instructor
        self.codigo_curso = codigo_curso


    def mostrar_info_curso(self):
        print(f"\n NOMBRE DEL CURSO: {self.nombre_curso}")
        print(f"\n NOMBRE DEL INSTRUCTOR: {self.instructor}")
        print(f"\n CODIGO DEL CURSO: {self.codigo_curso}")
        


