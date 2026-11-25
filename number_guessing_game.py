import random

print("===== NUMBER GUESSING GAME =====")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("\nCongratulations! You guessed it!")
        print("Attempts:", attempts)
        break
