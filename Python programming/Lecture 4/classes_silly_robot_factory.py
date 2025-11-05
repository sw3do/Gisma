import random

class Robots:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.quirks = random.choice(["loves dancing", "tells bad jokes", "collects shiny objects"])
        self.malfunctioned = False

    def introduce(self):
        return f"Hello, I am {self.name}, a robot from {self.year}. I have a quirky personality: I {self.quirks}!"

    def interact(self, other_robot):
        return f"{self.name} is interacting with {other_robot.name}!"
    
    def malfunction(self):
        self.malfunctioned = True
        return f"{self.name} has malfunctioned! Please service me."
    
    def status(self):
        if self.malfunctioned:
            return f"{self.name} is currently malfunctioning."
        else:
            return f"{self.name} is functioning normally."
        
        
robot1 = Robots("RoboMax", 2023)
robot2 = Robots("CyberNinja", 2024)
robot3 = Robots("TechBot", 2022)

print(robot1.introduce())
print(robot2.introduce())
print(robot3.introduce())

print("\n" + robot1.interact(robot2))
print(robot2.interact(robot3))

print("\n" + robot1.malfunction())
print(robot1.status())
print(robot2.status())