import random
from replit import clear
from art import logo



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a Draw!"
  elif computer_score == 0:
    return "Lose, Opponent has Blackjack!"
  elif user_score == 0:
    return "You won, You have a Blackjack!"
  elif user_score > 21:
    return "You lose, You went over."
  elif computer_score > 21:
    return "You win, Opponent went over."
  elif user_score > computer_score:
    return "You Win"
  else:
    return "You Lost"


def keep_playing():

  print(logo)

  user_card = []
  computer_card = []

  keep_going = True 


  for i in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())


  while keep_going:


    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f" Your cards: {user_card}, current score: {user_score}")
    print(f" Computer's first card is: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      keep_going = False
    else:
      another_card = input("Do u want to get another card type 'y' for yes or 'n' to pass: ")
      if another_card == "y":
        user_card.append(deal_card())
      else:
        keep_going = False


  while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)


  print(f"Your final hand: {user_card}, final score: {user_score}")
  print(f"Computer's final hand: {computer_card}, Computer final score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you wnat to play Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  keep_playing()
