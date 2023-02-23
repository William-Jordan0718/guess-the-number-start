#Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
from art import logo
print(logo)

# Allow the player to submit a guess for a number between 1 and 100.
input("Welcome to the Guessing Game!")

random_number = random.randint(1, 100)
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 

difficulty = input("Please choose difficulty 'easy' or 'hard'.")
if difficulty == 'easy':
  lives = 10
if difficulty == 'hard':
  lives = 5
    
while lives > 0:
  guess = int(input("Guess a number from 1 - 100.\n"))
  if guess == random_number:
    print("You Win!")
    print(f"The correct answer is {random_number}")
  elif guess > random_number:
    print("Too High")
    lives - 1
  elif guess < random_number:
    print("Too Low")
    lives - 1
  if lives == 0:
    print("Game Over. Out of Lives!")
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

