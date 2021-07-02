############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):  ### if the last no is 20 then it's only read till 19 if we want 20 we need to say 21.
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5)
# # print(dice_num)  ### This line is added for checking the
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:  ### added + sign
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))  ### added int command.
# if age > 18:
#   print(f"You can drive at age {age}.") ### added f string.
# ###else:
#   ###print("You are too young, You can't drive.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages) ###  Added this line 
# word_per_page = int(input("Number of words per page: "))  ### Removed one equal sign 
# print(word_per_page)  ### Added this line
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)     ### indented inside the loop
#   print(b_list)


# mutate([1,2,3,5,8,13])







########### debugging  1 ##############

number = int(input("Which number do you want to check?  "))

if number % 2 == 0:  ### Added one more equal sign 
  print("This is an even number.")
else:
  print("This is an odd number.")
  







########### debugging  2 ##############

year = int(input("Which year do you want to check?"))  ### Added int function

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
  
  
  
  
  
  
########### debugging  3 ##############

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:     ### changed or to and
    print("FizzBuzz")
  elif number % 3 == 0:                       ### changed if to elif
    print("Fizz")
  elif number % 5 == 0:                       ### changed if to elif
    print("Buzz")
  else:
    print(number)                             ### removed square brackets 
    
 
