import random

class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.weakness = weakness
    
    def introduce(self):
        return f"I am {self.name}! My power is {self.power}, but beware of my weakness: {self.weakness}!"
    
    def battle_cry(self):
        return f"{self.name} charges with {self.power.upper()}!"
    
    @staticmethod
    def fight(hero_1, hero_2):
        return random.choice([f"{hero_1.name} wins!", f"{hero_2.name} wins!"])
       
hero1 = Superhero("Thunderbolt", "Electricity", "Water")
print(hero1.introduce())
print(hero1.battle_cry())

hero2 = Superhero("Shadowstrike", "Invisibility", "Light")
print(hero2.introduce())
print(hero2.battle_cry())

print(Superhero.fight(hero1, hero2))