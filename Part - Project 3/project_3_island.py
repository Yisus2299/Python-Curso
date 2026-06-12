# island with if, elif, and else

print("Welcome to Treasure Island")

path = input("You are at a crossroads with two paths, which do you choose: L or R? ")
if path == "L":
    print("You chose the left path and opened a door that led you to an ocean.")
    water = input("You can choose to swim or wait. S or W? ")
    if water == "S":
        print("You chose to swim and survived. While swimming you see a shore in the distance and stay there.")
        doors = input("Once you reach the shore you see three doors, which do you choose: R or Y or B? ")
        if doors == "R":
            print("You chose the red door and found a lion. Game over.")
        elif doors == "Y":
            print("You chose the yellow door and found a dragon. Game over.")
        elif doors == "B":
            print("You chose the blue door and found the path back home. Game over.")
    elif water == "W":
        print("You chose to wait and drowned. Game over.")
elif path == "R":
    print("You chose the right path and found a tree. Game over.")
else:
    print("Game over.")


