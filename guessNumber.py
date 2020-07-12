import random
import sys

numberToGuess = random.randrange(1, 100)
userNumber = None

while userNumber != numberToGuess:
    print("Enter a proposal :")
    try:
        userNumber = int(input())
    except ValueError:
        print("You did not enter a number")
        sys.exit(1)

    if userNumber > numberToGuess:
        print("The number is smaller")
    elif userNumber < numberToGuess:
        print("The number is greater")

print("Well done you find the number")
