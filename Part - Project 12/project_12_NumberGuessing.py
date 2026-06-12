
from random import randint

# constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Check the user's guess against the actual answer and return remaining turns."""
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def choose_difficulty():
    level = input("Choose a difficulty: 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game\n")
    print("I'm thinking of a number between 1 and 100.\n")
    answer = randint(1, 100)
    print(f"The correct answer is: {answer}")

    turns = choose_difficulty()

    # repeat guessing until correct or out of turns
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of turns. You lose.")
            break
        elif guess != answer:
            print("Guess again")


if __name__ == "__main__":
    game()



