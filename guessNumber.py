import random

numberToGuess = random.randrange(1, 100)
userNumber = None

while userNumber != numberToGuess:
    print("Enter a proposal :")
    userNumber = int(input())
    if userNumber > numberToGuess:
        print("The number is smaller")
    elif userNumber < numberToGuess:
        print("The number is greater")

print("Well done you find the number")
