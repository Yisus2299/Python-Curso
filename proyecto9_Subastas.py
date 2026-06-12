#1- ask the user for input
#2- store the information in a dictionary {name: price}
#3- whether new bids should be added
#4- compare the bids in a dictionary

def winner_bet(dictionary_bets):
    winner = ""
    winning_bid = 0
    for gambler in dictionary_bets:
        amount_bid = dictionary_bets[gambler]
        if amount_bid > winning_bid:
            winning_bid = amount_bid
            winner = gambler

    print(f"The winner is: {winner} with a bid of ${winning_bid}.")

bets = {}

should_continue = True

while should_continue:
    name = input("What is your name?\n")
    price = int(input("What is your bid?: $"))
    bets[name] = price
    wanna_continue = input("Is there another bid? Type 'Yes' or 'No'.  \n").lower()
    if wanna_continue == "no":
        should_continue = False
        winner_bet(bets)
    elif wanna_continue == "yes":
        print("\n" * 20)