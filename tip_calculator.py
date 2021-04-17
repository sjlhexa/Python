print("Welcome to tip calculator.")
x = float(input("what was the total bill? $"))
y = int(input("What percentage tip would you like to give 10, 12, or 15? "))
z = int(input("How many people to split the bill? "))


total_bill = (y /  100 * x + x) / z

final_amount = round(total_bill, 2)
print(f"Each person should pay $ {final_amount}")
