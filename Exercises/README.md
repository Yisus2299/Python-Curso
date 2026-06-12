# Python Practice Exercises

A collection of Python exercises covering fundamental programming concepts including dictionaries, lists, loops, conditionals, and a "Higher or Lower" game.

## Overview

This folder contains various Python exercises designed to practice and reinforce programming concepts. The exercises range from basic dictionary operations to building an interactive "Higher or Lower" style game.

## Project Structure

```
Exercises/
├── exercises_to_practice.py    # Main exercise file with multiple practice problems
├── poo_exercises.py            # Object-oriented programming exercises
├── pizza_practice_Elif.py     # Conditional exercises (if/elif/else)
└── README.md                   # This file
```

## Exercise Categories

### 1. List Operations

Basic list manipulation and string concatenation:

```python
# Create a list from user input
lista = []
while True:
    words = input("Write something (Empty Enter to finish): ")
    if words == "":
        break
    lista.append(words)

print(lista)
```

```python
# String concatenation from list
lista = ['a','b','c','d','e']
practice = ""
for letter in lista:
    practice += letter
print(practice)  # Output: abcde
```

### 2. Dictionary Operations

Working with key-value pairs:

```python
# Display dictionary, modify values, access specific keys
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict['profession'] = 'Doctor'
my_dict['age'] = 40
print(my_dict)
print(my_dict['city'])
```

```python
# Add, update, delete dictionary items
users = {'id1': 'admin', 'id2': 'user', 'id3': 'guest'}
users['id4'] = "reader"           # Add new item
users.update({'id3': "view only"}) # Update existing
del users['id5']                   # Delete item
# Alternative: users.pop('id3')
```

```python
# Dictionary comprehension
grades = {'Ana': 8, 'Pedro': 4, 'Luis': 6}
approved = {grade: name for name, grade in grades.items() if grade >= 5}
print(approved)
```

### 3. Conditional Exercises (If/Elif/Else)

Grading system based on scores:

```python
student_scores = {
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
        student_grades[name] = "could improve"
    else:
        student_grades[name] = "failed"
print(student_grades)
```

### 4. Product Dictionary

Iterating over dictionary items:

```python
products = {"Apple": 10, "Pear": 15, "Melon": 20}
for fruit, price in products.items():
    print(f"Fruit: {fruit}, price: {price}.")
```

---

## Higher or Lower Game

A complete interactive game comparing social media accounts and celebrities.

### Overview

The game presents two options (A and B) and asks the user to guess which one has more followers. After each correct guess, the score increases and the game continues with a new option.

### Game Data

```python
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
    # ... more accounts
]
```

### Game Functions

#### Choice Function

```python
def choice(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description} From {account_country}"
```

Displays formatted account information.

#### Check Function

```python
def revisar(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"
```

Compares follower counts and validates user's guess.

### Game Loop

```python
should_continue = True
score = 0

while should_continue:
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    
    print(f"Compare A: {choice(account_a)}")
    print("vs")
    print(f"Compare B: {choice(account_b)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    answer = revisar(guess, a_follower, b_follower)
    
    if answer:
        score += 1
        print(f"You got it right! Current score: {score}")
        account_a = account_b  # B becomes the new A
        account_b = random.choice(data)  # New B
        while account_a == account_b:
            account_b = random.choice(data)
    else:
        print(f"You missed! Final score: {score}")
        should_continue = False
```

### Game Mechanics

1. Two random accounts are selected
2. User compares and guesses which has more followers
3. If correct: score increases, B becomes new A, new B is selected
4. If wrong: game ends, final score shown
5. The comparison chain continues (A always wins in previous round)

### Key Concepts Practiced

| Concept | Example in Code |
|---------|-----------------|
| Random Selection | `random.choice(data)` |
| Dictionary Access | `account["follower_count"]` |
| While Loops | `while should_continue:` |
| Conditionals | `if a_follower > b_follower:` |
| Functions | `def choice(account):` |
| String Formatting | `f"Compare A: {choice(account_a)}"` |
| List Handling | `account_b = random.choice(data)` |

## Additional Exercise Concepts

### List Basics

```python
# Create list from input
words = []
while True:
    user_input = input("Enter word: ")
    if user_input == "":
        break
    words.append(user_input)
```

### String Concatenation

```python
# Method 1: Loop
text = ""
for char in ['h', 'e', 'l', 'l', 'o']:
    text += char

# Method 2: Join
text = "".join(['h', 'e', 'l', 'l', 'o'])
```

### Dictionary Comprehension

```python
# Filter dictionary
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v > 2}
# Result: {'c': 3, 'd': 4}
```

## Usage

Run individual exercise files:

```bash
# Main exercises
python exercises_to_practice.py

# OOP exercises (if file has main)
python poo_exercises.py

# Pizza/conditional exercises
python pizza_practice_Elif.py
```

Note: Some exercises contain commented-out code that serves as reference. Uncomment to test.

## Learning Outcomes

After completing these exercises, you should understand:

- ✅ List creation and manipulation
- ✅ Dictionary operations (add, update, delete)
- ✅ Conditional statements (if/elif/else)
- ✅ Loop structures (for, while)
- ✅ Function definition and usage
- ✅ String formatting
- ✅ File I/O (reading CSV)
- ✅ Basic game logic
- ✅ Random module usage

## License

(Just in case, this project is for educational purposes, i don't know own anything of all this plus it's just a practice.)