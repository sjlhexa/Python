from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")


all_bids = {}
def find_highest_bidder(bidding_record):
  highest_bid =  0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
go_on = True
while go_on:
  name = input("What is your name?: ")
  bid = int(input("What's your bid amount?: $"))
  all_bids[name] = bid
  go_on = input("Are there any other bidders? type 'yes' or 'no'.\n")

  
  if go_on == "no":
    bid_on = False
    find_highest_bidder(all_bids)
  elif go_on == "yes":
    clear()

#HINT: You can call clear() to clear the output in the console.
