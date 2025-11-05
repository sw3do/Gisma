class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
    
    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} is less hungry!")
    
    def play(self):
        self.happiness = min(100, self.happiness + 15)
        print(f"{self.name} is happier!")

    def status(self):
        return f"{self.name}'s hunger: {self.hunger}, happiness: {self.happiness}"
    
    def petDemand(self):
        if self.hunger > 70:
            return f"{self.name} is very hungry! Please feed me!"
        elif self.happiness < 30:
            return f"{self.name} is feeling sad! Let's play!"
        else:
            return f"{self.name} is content!"


my_pet = VirtualPet("Fluffy")
my_pet.feed()
my_pet.play()
print(my_pet.status())  
print(my_pet.petDemand())
