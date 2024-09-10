class Coche:
    marca = ""
    modelo = ""
    año = 0



    #METODO DEL CONSTRUCTOR
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    

    #PRIMER METODO
    def mostrar_info(self):
        print("MARCA:", self.marca)
        print("MODELO:", self.modelo)
        print("AÑO:", self.año)  
    #SEGUNDO METODO

        

