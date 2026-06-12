# invented project "escape the maze"
# there is no escape but this really illustrates that without a while loop, it would end as soon as it says "there is a wall there" and similar
position = 0
exit = 6

while position != exit:
    print("You are at:", position)
    move = input("Type left or right: ").lower()
    if move == "left":
        new = position - 1
        if new < 0:
            print("You cannot leave the maze.")
        elif new == 2 or new == 5:
            print("There is a wall there.")
        else:
            position = new
    elif move == "right":
        new = position + 1
        if new > 6:
            print("You cannot leave the maze.")
        elif new == 2 or new == 5:
            print("There is a wall there.")
        else:
            position = new
    else:
        print("Type only 'left' or 'right'.")
print("Congratulations, you escaped!")