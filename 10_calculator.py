from art import logo
#Add
def add(n1,n2):
  return n1 + n2

#Subtract 
def Subtract(n1,n2):
  return n1 - n2

#Multiply
def Multiply(n1,n2):
  return n1 * n2

#Divide
def Divide(n1,n2):
  return n1 / n2


operations = {
  "+": add,
  "-": Subtract,
  "*": Multiply,
  "/": Divide,
}

def cal():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for i in operations:
    print(i)

  keep_on = True
  while keep_on:
    opertaion_input = input("Choose an operations: ")
    num2 = float(input("What's the next number?:"))
    calculation_function = operations[opertaion_input]
    output = calculation_function(num1,num2)

    print(f"{num1} {opertaion_input} {num2} = {output}")

    if input(f"Type 'y' to continue with {output}, or type 'n' to start a new calculation.: ") == "y":
      num1 = output
    else:
      keep_on = False
      cal()
cal()      
