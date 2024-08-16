import random

target= random.randint(1,100)

while True:
    userChoice=input("Guess a number between 1 and 100 or Quit(Q/q): ")
    if(userChoice == "Q"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Congratulations! You have guessed the number")
        break
    elif(userChoice<target):
        print("Try again! Your number is too small. Please guess a higher number")
    else:
        print("Try again! Your number is too big. Please guess a lower number")

print("----GAME OVER----")        