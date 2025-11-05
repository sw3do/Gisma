
catCounter = 0

def grumpy_cat(): 
    """Return a grumpy cat response based on counter."""
    global catCounter
    catCounter += 1
    
    if catCounter == 1:
        return "I'm okay thank you"
    elif catCounter == 2:
        return "Leave me alone"
    elif catCounter == 3:
        return "Go away"
    elif catCounter == 4:
        return "Get lost"
    elif catCounter == 5:
        catCounter = 0
        return "Meh"
    else:
        return "Nope"


while True:
    user_input = str(input("Ask the cat how are you? (or type 'break' to exit): ")).lower()
    
    if user_input == "break":
        print("Goodbye!")
        break
    
    if user_input == "how are you?" or user_input == "how r u?" or user_input == "how are u?" or user_input == "how do you do?":
        response = grumpy_cat()
        print(f"Grumpy Cat says: {response}")
        
        if catCounter == 0:
            print("Grumpy Cat has had enough! Goodbye!")
            break
    else:
        print("Ask me 'how are you?' to get a response!")