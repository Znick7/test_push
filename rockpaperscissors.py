import random
#hello_world
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, or Scissors? Press Q to quit ").lower()
    if user_input == "q":   
        break
    if user_input not in ["rock", "paper", "scissors"]:
        print("Please type Rock, Paper, or Scissors")
        continue
    random_number = random.randint(0,2)
    # 0 is rock   1 is paper   2 is scissors
    computer_pick= options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("you lost!")
        computer_wins += 1

print("You won", user_wins, "times")      
print("Computer won", computer_wins, "times")
