class Celular: #las clases son como un molde para crear objetos
    def __init__(self, marca, modelo, camara): #el constructor es la funcion que se ejecuta cuando se crea un objeto
        self.marca = marca #self es el objeto que se esta creando y marca, modelo y camara son los atributos del objeto
        self.modelo = modelo #self.marca es el atributo del objeto
        self.camara = camara #self.modelo es el atributo del objeto
        
    def llamar(self):
        print(f"estas llamando desde un {self.modelo}")

    

celular1 = Celular("Samsung", "S23", "48mp") #celular1 es el objeto que se esta creando
celular2 = Celular("Apple", "Iphone 15 pro", "58mp") #celular2 es el objeto que se esta creando

celular1.llamar()



