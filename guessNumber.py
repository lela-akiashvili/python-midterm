from random import randint

# Generate a random target number between 1 and 50 (inclusive).
num = randint(1, 50)

i = 1
max_attempts = 5

print(f"guess the number from 1 to 50 (you have {max_attempts} attempts)!")

# Main game loop: keep asking while we still have attempts left.
while i <= max_attempts:

    # Read the player's guess and validate it's an integer.
    # If conversion to int fails, notify the user and let them try again
    try:
        guess = int(input(f"Try {i}. Your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Compare the guess to the target and give feedback.
    if guess == num:
        print(f"You guessed it! The number is {num}.")
        break
    elif guess > num:
        print("Too high!")
    else:
        print("Too low!")

    # Increment attempt counter after an incorrect valid guess.
    i += 1
    print()

# inform the player they lost and reveal the number.
if i > max_attempts:
    print(f"You lost! You used all {max_attempts} attempts. The number was {num}.")
