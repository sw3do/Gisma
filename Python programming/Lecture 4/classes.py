
class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    
x = Cars("Toyota", "Corolla", 2020)
print(x.display_info())


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
            print(f"{self.name} says hello!")
            
dog = Pet("Buddy", 3)
dog.speak()
print(dog.age)