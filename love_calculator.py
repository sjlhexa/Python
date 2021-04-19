# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


lower1 = name1 .lower()
lower2 = name2 .lower()
name = lower1 + lower2


t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")


true = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l + o + v + e


score = int(str(true)) + int(str(love))

print(score)

if (score < 10) or (score > 90):
  print(f"Your love score is {score}, you go like coke and metos. ")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")
