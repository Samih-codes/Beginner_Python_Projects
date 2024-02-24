from replit import clear
from art import logo

print(logo)

dict_bids = {}

print("Welome to the secret auction event!")
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict_bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == 'yes':
        clear()
    else:
        break

winner_name = max(dict_bids, key=dict_bids.get)
winning_bid = dict_bids[winner_name]

print(f"The winner is {winner_name} with a bid of ${winning_bid}.")
