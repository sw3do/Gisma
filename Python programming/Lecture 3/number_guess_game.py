import random

while True:
    try:
        user_input = int(input("Guess a number between 1 and 10 (or 0 to quit): "))

        if user_input == 0:
            print("Game over! Goodbye!")
            break

        if user_input < 1 or user_input > 10:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        random_number = random.randint(1, 10)

        if user_input == random_number:
            print("🎉 Congratulations! You guessed the correct number.")
        else:
            print(f"Sorry, the correct number was {random_number}. Try again!")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
