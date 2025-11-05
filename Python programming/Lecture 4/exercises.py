class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
p1 = Person("Alice", 30)
print(p1.greet())
print(p1.age)
print(p1.name)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height



r1 = Rectangle(5, 10)
print(f"Area of rectangle: {r1.area()}")
print(f"Width of rectangle: {r1.width}")
print(f"Height of rectangle: {r1.height}")

class BankAccount: 
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance


acc = BankAccount("John Doe", 1000)
print(f"Initial balance: {acc.balance}")
print(f"Balance after deposit of 500: {acc.deposit(500)}")
print(f"Balance after withdrawal of 300: {acc.withdraw(300)}")
print(f"Balance after withdrawal of 1500: {acc.withdraw(1500)}")
print(f"Account holder: {acc.account_holder}")


class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
car1 = Cars("Honda", "Civic", 2022)
print(car1.description())

car2 = Cars("Ford", "Mustang", 2021)
print(car2.description())