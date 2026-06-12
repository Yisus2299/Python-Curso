# scope and the project called: Guess the number

enemies = 1

def increment():
    enemies = 2
    #print(f"the enemies inside are: {enemies}")

#increment()
#print(f"The enemies outside the function: {enemies}")

# local scope: it exists inside the function.

def drink_potion():
    strenght_potion = 2 # strenght_potion is defined inside drink_potion.
    # That variable only “lives” inside that function; outside it you should not use it (NameError if you try to access it).
    print(strenght_potion)

#drink_potion()

# global scope: it exists at the file level (outside functions).

player_health = 10 # player_health = 10 is in the “global scope”
# so it can be used from anywhere in the file (including functions), as long as there is no local variable with the same name that shadows it.

def game():
    def drink_potion():
        strenght_potion = 2
        print(player_health) # we can use player_health inside the function because it is in the global scope, but we cannot use strenght_potion outside the function because it is in the local scope

    drink_potion()
#game() # in this case we put drink_potion inside another function, so we must call game() to execute it

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# There is no block scope in Python

level = 3
enemies = ['aliens', 'zombies', 'vampires']

def crear_enemigo():
    new_enemy = ""
    if level < 5:
        new_enemy += enemies[0]
    return print(f"the enemy is: {new_enemy}")
#crear_enemigo()

#===================================================================================================================================================================#

# write a function that says whether a number is prime or not:

def is_prime(num): # creates a function that receives a number num and decides if it is prime.
    # quick case: numbers less than 2
    if num < 2: # if the number is less than 2 it does not count as prime
        return False
    for i in range(2, num): # search for divisors: generates values i = 2, 3, 4, ... until reaching the given number
        # we start at 2 because 1 does not count, and advance 2,3,4,5,6,7... until reaching the assigned number
        if num % i == 0: # if the number divides evenly then:
            return False  # If you find a divisor, it is NOT prime
    return True #  # If you find a divisor, it is NOT prime

#print(is_prime(2)) # we use number 2 as an example because it is prime and it works

#====================================================================================================================================================================#
# I paused at How to modify a global variable - video 89 (change bank password isis :u)
# Modifying the Global Scope
enemies = 1

def increment_enemies(enemy):
    print(f"the enemies inside the function: {enemies}")
    return enemy + 1

enemies = increment_enemies(enemies)
#print(f"enemies outside the function: {enemies}")

#=====================================================================================================================================================================#

# global constants
# this means that URLs like: GOOGLE, FACEBOOK, INSTAGRAM and mathematical formulas like PI are almost always uppercase and we can refer to them
# later if they are defined before the function we want to create


