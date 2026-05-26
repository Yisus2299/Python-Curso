#crear tus propias clases
#Constructor def __init__(self)

#aprendimos a crear una funcion constructor, agregar metodos a las clases y crear clases


# class User: 
#     def __init__(self, user_id, username): #self es lo que esta siendo inicializado adentro de la funcion
#        self.id = user_id
#        self.username = username
#        self.followers = 0
#        self.following = 0

#     #agregar metodos a las clases

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# #cada vez que la funcion constructor se emplea, se ejecuta lo de adentro de la funcion
# user_1 = User("001", "Jesus",)
# user_2 = User("002", "Alekk",)

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

# class Animal:

#         def eyes(self):
#             self.num_eyes = 2
#             return self.num_eyes

#         def breathe(self):
#             print("si respira")

# class Fish(Animal):

#         def __init__(self):
#              super().__init__()
        
#         def eyes(self):
#             return super().eyes()
            

#         def breathe(self):
#               super().breathe() 
#               print("debajo del agua")

#         def nadar(self):
#             print("Se mueve adentro del agua")
    
# nemo = Fish()
# print(nemo.eyes())
# nemo.nadar()
# nemo.breathe()

#=========================================================================================================================#

piano_keys = ['a','b','c','d','e','f','g']

#print(piano_keys[2:5]) #slice, el primero contamos desde 0 y para el segundo contamos desde 1
#print(piano_keys[2:])
#print(piano_keys[:5])
print(piano_keys[2:5:2])
                #c 


