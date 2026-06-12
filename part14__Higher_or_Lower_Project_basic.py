
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
]

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_desc}, From {account_country}")



def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    
    print(f"Compare A: {format_data(account_a)}. ")
    print("VS")
    print(f"Compare B: {format_data(account_b)}. ")

    guess = input("Quien tiene mas seguidores? Escribe 'A' o 'B':  ").lower()

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    if is_correct:
        score += 1
        print(f"Acertaste, tienes razon. Puntaje actual {score}")
    else:
        print(f"Fallaste, lo siento. Puntaje actual {score}")
        should_continue = False
        