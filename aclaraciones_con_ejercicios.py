# list = []

# while True:
#     words = input("Write something (Empty Enter to finish):\n")
#     if words == "":
#         break
#     lista.append()

# print(lista)

# text = ""
# text += input("First part: ") + " "
# text += input("Second part: ")

# print(f"{text}")

# lista = ['a','b','c','d','e']

# practice = ""

# for letter in lista:
#     practice += letter

# print(practice)

# dictionary exercises

#1- display the whole dictionary on screen, change the age, the profession and only display the city.

'''my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

my_dict['profession'] = 'Doctor'

my_dict['age'] = 40

print(my_dict)
print(my_dict['city'])'''

#2- grade exercise and show what to do depending on the case

'''student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name, grade in student_scores.items():
    if grade >= 91:
        student_grades[name] = "Excellent"
    elif grade >= 81:
        student_grades[name] = "Not bad"
    elif grade >= 71:
        student_scores[name] = "could improve"
    else:
        student_grades[name] = "failed"
print(student_grades)'''

# Create a product-price dictionary and then print each product and its price using .items().

# products = {"Apple": 10, "Pear": 15, "Melon": 20}

# for fruit, price in products.items():
#     print(f"Fruit: {fruit}, price: {price}.")


# grades = {'Ana': 8, 'Pedro': 4, 'Luis': 6}

# approved = {grade: name for name, grade in grades.items() if grade >= 5}

# print(approved)

''''users = {'id1': 'admin', 'id2': 'user', 'id3': 'guest', 'id5': "I don't know"}


users['id4'] = "reader" # add items to a dictionary
users.update({'id3': "view only"}) # update something in a dictionary
del users['id5'] # delete items from a dictionary, another option to remove: #users.pop('id3')

#print(users)'''

#====================================================================================================================#

import random


data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Facebook',
        'follower_count': 350,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Two Door Cinema Club',
        'follower_count': 150,
        'description': 'Music Band',
        'country': 'United Kingdom'
    }
] # first we have the dictionary with all the information we will use in the exercise

account_a = random.choice(data) # create a variable for option A that selects random information
account_b = random.choice(data) # create a variable for option B that selects random information


def choice(account): # create a function to store the name, description and country in variables
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, {account_description} From {account_country}") # return the name, description and country



def revisar(user_guess, a_follower, b_follower): # create a function that contains a conditional to check the followers
    if a_follower > b_follower: # if A has more followers than B, in short, return the result for letter A
        return user_guess == "a"
    else:
        return user_guess == "b" # same for B



should_continue = True # create a variable for the while loop so the game continues
score = 0 # create a variable initialized at 0 to store the score if we guess or miss


while should_continue: # start the while loop where we will store the follower variables, otherwise it will not work
 # here is where we store the two follower-related variables, to be able to call the conditional function
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

# display on screen the function which also calls the random options and shows one option
    # print(f"Compare A: {choice(account_a)}")
    # print("vs")
    # print(f"Compare B: {choice(account_b)}")
    # ask on screen which option can be greater
    # guess = input("Who has more followers? Type 'A' or 'B':  ").lower()
    
    # create a variable that immediately applies the conditional
    # answer = revisar(guess, a_follower, b_follower )

    # if answer:
    #     score+=1 # if we guess correctly the score increases
    #     print(f"You got it right, you are correct. Current score {score}")
    #     account_a = account_b
    #     # In “Higher or Lower”, the usual rule is: the option that was B becomes 
    #     # the new A in the next question (the “anchor” you already know). That is why you copy the reference from B into A.
    #     account_b = random.choice(data) # The new option to compare is another random account from the list. It is the new “B” that the player must compare with the one that is now A.
    #     while account_a == account_b:
    #         account_b = random.choice(data)
    #     # If chance repeats the same account that is already A, you would have the same thing twice on screen and the game would not make sense. This loop re-selects B until it is different from A.
    # else:
    #     print(f"You missed, sorry. Current score {score}")
    #     should_continue = False # as soon as you fail, the loop ends and the game finishes
    #     break

#==========================================================================================================================================================================================================#











