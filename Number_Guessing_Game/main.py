# My Number Guessing Game Objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def random_number():
    """Picks a random number between 1 and 100"""
    return random.randint(1, 100)

def make_guess(hidden_number, attempts_remaining):
  while attempts_remaining > 0:
      user_guess = int(input("Make a guess: "))
      attempts_remaining -= 1
  
      if user_guess == hidden_number:
          return f"You got it! The answer was {hidden_number}"
      elif user_guess < hidden_number:
          print("Too low.")
          if attempts_remaining > 0:
              print("Guess again.")
      else:
          print("Too high.")
          if attempts_remaining > 0:
              print("Guess again.")
  
      if attempts_remaining > 0:
          print(f"You have {attempts_remaining} attempts remaining to guess the number.")
  
  return f"You've run out of guesses. The answer was {hidden_number}."


def play_game():
    print(logo)
    print("Welcome to the Number Guesser game! \nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts_remaining = 10
    else: 
        attempts_remaining = 5

    print(f"You have {attempts_remaining} attempts remaining to guess the number.")

    hidden_number = random_number()
    result = make_guess(hidden_number, attempts_remaining)
    print(result)

play_game()

