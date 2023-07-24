import random

print("Guess the NUMBER GAME!")

number_to_guess = random.randint(1, 1000000)
count = 0

while True:
    count += 1
    try:
        guessed_number = int(input("Please enter a number between 1 and 1,000,000: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if guessed_number < 1 or guessed_number > 1000000:
        print("Number out of range! Please enter a number between 1 and 1,000,000.")
        continue
    elif number_to_guess < guessed_number:
        print("Too high!")
    elif number_to_guess > guessed_number:
        print("Too low!")
    else:
        print("Correct!")
        break

print("It took you", count, "attempts to guess the number correctly.")
