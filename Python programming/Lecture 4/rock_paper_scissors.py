import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!" 
        
def play_game():
  try:
      user_choice = input("Enter rock, paper, or scissors: ").lower()
      if user_choice not in ['rock', 'paper', 'scissors']:
          raise ValueError("Invalid choice. Please choose rock, paper, or scissors.")
      
      game = RockPaperScissors()
      computer_choice = game.get_computer_choice()
      print(f"Computer chose: {computer_choice}")
      
      result = game.determine_winner(user_choice, computer_choice)
      print(result)
  except ValueError as ve:
      print(ve)
    
    
play_game()