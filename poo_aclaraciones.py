class Celular: # classes are like a mold for creating objects
    def __init__(self, marca, modelo, camara): # the constructor is the function that runs when an object is created
        self.marca = marca # self is the object being created and marca, modelo, and camara are the object's attributes
        self.modelo = modelo # self.marca is the object's attribute
        self.camara = camara # self.modelo is the object's attribute
        
    def llamar(self):
        print(f"you are calling from a {self.modelo}")

    

celular1 = Celular("Samsung", "S23", "48mp") # celular1 is the object being created
celular2 = Celular("Apple", "Iphone 15 pro", "58mp") # celular2 is the object being created

celular1.llamar()



