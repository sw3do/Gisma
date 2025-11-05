import random

def game(text):
    styles = ['normal', 'vowels', 'upper', 'lower', 'reverse']
    vowels = "aeiouAEIOU"
    choice = random.choice(styles)
    if not isinstance(text, str):
        return "Invalid input. Please enter a string."
    elif choice == 'normal':
        return text
    elif choice == 'vowels':
        return ''.join(random.choice("abcyzx") if char in vowels else char for char in text)
    elif choice == 'upper':
        return text.upper()
    elif choice == 'lower':
        return text.lower()
    elif choice == 'reverse':
        return text[::-1]
    else:
        return "Error: Unknown style"
    
    
  
        
input_text = input("Enter text for the robot parrot: ")
output_text = game(input_text)
print(f"Robot parrot output: {output_text}")
