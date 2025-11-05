import random

while True:
    try:
        user = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
        if user == 'quit':
            break
        chooses = ['rock', 'paper', 'scissors']
        if user not in chooses:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue
        computer = random.choice(chooses)
        print(f"Computer chose: {computer}")
        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("You win!")
        else:
            print("You lose!")
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        break
    except Exception as e:
        print(f"An error occurred: {e}")

        