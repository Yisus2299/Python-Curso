# create your own classes
# Constructor def __init__

# we learned to create a constructor function, add methods to classes, and create classes


# class User: 
#     def __init__(self, user_id, username): # self is what is being initialized inside the function
#        self.id = user_id
#        self.username = username
#        self.followers = 0
#        self.following = 0

#     # add methods to classes

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# # every time the constructor function is used, the inside of the function executes
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
#             print("it breathes")

# class Fish(Animal):

#         def __init__(self):
#              super().__init__()
        
#         def eyes(self):
#             return super().eyes()
            

#         def breathe(self):
#               super().breathe() 
#               print("underwater")

#         def swim(self):
#             print("It moves inside the water")
    
# nemo = Fish()
# print(nemo.eyes())
# nemo.swim()
# nemo.breathe()

#=========================================================================================================================#

piano_keys = ['a','b','c','d','e','f','g']

#print(piano_keys[2:5]) # slice, the first index counts from 0 and the second counts from 1
#print(piano_keys[2:])
#print(piano_keys[:5])
print(piano_keys[2:5:2])
                # c
