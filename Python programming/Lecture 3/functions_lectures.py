# import math # or from math import exp sqrt, pow, etc.
from math import exp
import datetime

def hello_world(message):
    print(message)


hello_world("print")
 
def add_values(a, b):
     return a + b
 
result = add_values(5, 10)
print("Sum:", result)

def multiply_values(a, b):
    return a * b
product = multiply_values(4, 5)
print("Product:", product)

def divide_values(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

quotient = divide_values(20, 4)
print("Quotient:", quotient)

def name_of_function(name = 'World'):
    return f"Hello, {name}!"

print(name_of_function())
print(name_of_function("Alice"))

def calculate_exp_area(number = 1):
    """If are you using import math you need to change like 'math.exp(number)'."""
    return exp(number)


print(calculate_exp_area())
print(calculate_exp_area(3))

def current_datetime():
    return datetime.datetime.now()

print("Current date and time:", current_datetime())

def factorial(n):
    """
    Return the factorial of a number n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 4

print(f"Factorial of {number}:", factorial(number))