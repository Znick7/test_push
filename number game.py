import random
top = input("Type a number: ")
if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number next time")
    quit()

r = (random.randint(0,top))
guesses = 0
while True:
    guesses += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == r:
        print("You got it!")
        break
    else:
        if user_guess > r:
            print("Too High!")
        else:
            print("Too Low!")
print("You got it in", guesses, " guesses!")    

