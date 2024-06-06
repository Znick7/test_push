import random

user_wins = 0
compute_wins = 0

while True:
    user_input = input("Type Rock, Paper, or Scissors? Press Q to quit ").lower()
    if user_input == "q":   
        break
    if user_input not in ["rock", "paper", "scissors"]:
        print("Please type Rock, Paper, or Scissors")
        continue

print("lol")