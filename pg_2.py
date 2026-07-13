import random
import secrets

secret_number = random.randint(1, 10)
guess = 0
print("im thinking of a number between 1 and 10 can you guess it!")
while guess != secret_number:
    guess = int(input("guess a number between 1 and 10: "))
    if guess < secret_number:
        print("you guessed too low,try again")
    elif guess > secret_number:
        print("you guessed too high,try again")
    else:
        print("you guessed correctly")