from art import logo , vs
from game_data import data 
import random
from replit import clear



def Formatting_data(account):
  """Format data into readable bits"""
  name = account["name"]
  country = account["country"]
  description = account["description"]
  return f"{name} a {description} from {country}"



def Check_answer(guess, a_followers,b_followers):
  """takes user guess and and followers count of both accounts and compair"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"



#Print logo
print(logo)
score = 0
keep_going = True
account_b =  random.choice(data)

#Make the game repitable
while keep_going:
  #Get account 
  account_a =  account_b
  account_b =  random.choice(data)
  while account_a ==  account_b:
    account_b = random.choice(data)

  print(f"Compair A : {Formatting_data(account_a)}.")
  print(vs)
  print(f"Against B : {Formatting_data(account_b)}.")

  #Ask the user for a guess
  guess = input("Who have more followers enetr 'A' or 'B' :  ").lower()



  #




  #Get followers count
  a_followers_count = account_a["follower_count"]
  b_followers_count = account_b["follower_count"]
  is_correct = Check_answer(guess,a_followers_count,b_followers_count)

#Clear the screen
  clear()
  print(logo)
  #Give user a feedback
  #Keeping track of the score
  if is_correct:
    score += 1
    print(f"You're right! , Current score {score}.")

  else:
    keep_going = False
    print(f"Sorry that,s wrong. Final score {score}.")
