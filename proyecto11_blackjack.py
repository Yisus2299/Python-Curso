# 1 - create a function deal_card() that uses a list of values representing cards and returns a random card
# first we import the random module so the selected card is random

import random

def deal_card():  # when called, this function will return a number that represents the value of a card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Function to calculate the score of a hand
def calculate_score(cards):
    # If the hand is a blackjack (two cards that add up to 21) return 0 as a special marker
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If there is an ace (11) and the total is over 21, convert one ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Compare user and computer scores and return the game result message
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, the opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "The opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


# Main game logic grouped in a function for reuse
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False

    # Draw initial two cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Game loop: continue until the round ends
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} and your current score: {user_score}")
        print(f"The computer's first card is {computer_cards[0]}")

        # End conditions: natural blackjack for either side or user bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'yes' to get another card, type 'no' to pass: ").lower()
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws cards until it reaches 17 or has blackjack (0)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to keep playing Blackjack? Type 'yes' or 'no': ") == "yes":
    print("\n" * 20)
    play_game()





    