#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import Logo
print(Logo)


def user_turns():
  x = input("Choose a difficulty, Type 'easy' or 'hard' : ")
  diff = x.lower()
  if diff == "hard":
    return 5
  elif diff == "easy":
    return 10

def check(USER_GUESS , number,lives):
  if USER_GUESS > number:
    print("Too High")
    return lives - 1
  elif USER_GUESS < number:
    print("Too Low")
    return lives - 1
  elif USER_GUESS == number:
    print("You won")



def start():
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 to 100")
  num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
  number = random.choice(num)





  lives = user_turns()
  USER_GUESS = 0

  while USER_GUESS != number :

    print(f"You have {lives} attempts to guess the number")

    USER_GUESS = int(input("Make a guess:"))


    lives = check(USER_GUESS,number,lives)

    if lives == 0:
      print("You've run out of guesses, you lose")
      return

start()

