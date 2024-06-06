print("Welcome to my Quiz Game!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    quit()
count = 0

print("Lets play! I will ask you a series of questions. Answer them correctly to win!")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!") 
    count += 1  # count = count + 1
else:
    print("Incorrect!") 
    count -= 1  # count = count - 1

answer = input("What is the capital of the state of GA ").lower()
if answer == "atlanta":
    print("Correct!") 
    count += 1  # count = count + 1
else:
    print("Incorrect!") 
    count -= 1  # count = count - 1

answer = input("What does USA stand for ").lower()
if answer == "united states of america":
    print("Correct!") 
    count += 1  # count = count + 1
else:
    print("Incorrect!") 
    count -= 1  # count = count - 1

answer = input("What is 1 + 1 ").lower()
if answer == "2":
    print("Correct!") 
    count += 1  # count = count + 1
else:
    print("Incorrect!") 
    count -= 1  # count = count - 1

print("You got " + str((count / 4) *100 ) + "% questions correct! ")