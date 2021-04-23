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

image = [rock, paper, scissors]


first = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if first >= 3 or first < 0:
  print("You type an invalid no you lose")
else:
  print(image[first])

  computer_choice = random.randint(0 , 2)
  print("Computer chose:")
  print(image[computer_choice])


  if first == 0 and computer_choice == 2:
    print("You Win!")
  elif first >= 3 or first < 0:
    print("You type an invalid no you lose")
  elif computer_choice == 0 and first == 2:
    print("You lose")
  elif computer_choice > first:
    print ("You lose")
  elif first > computer_choice:
    print("You Win!")
  elif computer_choice == first:
    print("It's a draw")
