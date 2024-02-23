import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

start = "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n "
user_choice = int(input(start))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Your number is invalid. Please try again!")

if user_choice in [0, 1, 2]:
    print("Computer chose:")
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)

    if user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 0 and computer_choice == 0:
        print("It is a draw")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 1 and computer_choice == 1:
        print("It is a draw")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == 2 and computer_choice == 2:
        print("It is a draw")
else:
    print(" ")

