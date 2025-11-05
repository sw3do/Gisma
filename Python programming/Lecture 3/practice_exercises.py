import math
import random

def calculate_square(number):
    """Return the square of a number."""
    return math.pow(number, 2)

print(calculate_square(4))

def calculate_maxnum(a, b):
    """Return the maximum of two numbers."""
    return max(a, b)

print(calculate_maxnum(10, 20))

def calculate_tax(amount):
    """Calculate 15%, %10, %20, %30 tax on the given amount."""
    if not isinstance(amount, (int, float)):
        return "Invalid amount. Please enter a number."
    if amount < 0:
        return "Amount cannot be negative."
    if amount <= 20000:
        return amount
    elif amount <= 20001 or amount <= 50000:
        tax = amount * 0.10
    elif amount <= 50001 or amount <= 100000:
        tax = amount * 0.20
    else:
        tax = amount * 0.30
    return tax

print(calculate_tax(15000))  # No tax
print(calculate_tax(20000))  # 20000
print(calculate_tax(35000))  # 10% tax
print(calculate_tax(75000))  # 20% tax
print(calculate_tax(150000)) # 30% tax
print(calculate_tax(-5000))  # Invalid amount
print(calculate_tax("abc"))  # Invalid amount


def reverse_string(s):
    """Return the reversed version of the input string."""
    if not isinstance(s, str):
        return "Invalid input. Please enter a string."
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"


def find_avg(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        return "Invalid input. Please enter a list of numbers."
    return sum(numbers) / len(numbers)

print(find_avg([10, 20, 30, 40]))  # Output: 25.0


def magic8ball():
    """ Magic 8-Ball Game."""
    user_input = input("Ask me the question: ")
    responses = [
       "Definitely yes",
       "Maybe",
       "Try again later",
       "Absolutely not",
       "Yes, in due time",
       "Cannot predict now",
       "Very doubtful",
       "Without a doubt"
    ]
    return random.choice(responses)

print(magic8ball())


"""

  Defined inside a function. Only accessible inside that function.
  Defined outside all functions. Accessible from anywhere in the program. To modify it inside a function, you must use the global keyword.
  Used in nested functions. Allows the inner function to modify a variable from the outer function using the nonlocal keyword.

"""


localValue = 5 # Global

def outer():
    outerValue = 10 # Local

    def inner():
        nonlocal outerValue # NoNLocal
        outerValue = 15
        return f"Outer Value: {outerValue}, Local Value: {localValue}"

    return inner()

print(outer())  # Output: Outer Value: 15, Local Value: 5


plusnumberlambda = lambda a, b : a + b

print(plusnumberlambda(3, 7))  # Output: 10



squarelambda = lambda i: i * i

print(squarelambda(4))         # Output: 16

# 1. Simple Arth. Opearations

artc = lambda x, y: x * y

print(artc(4, 5))  # Output: 20

# 2. Sorting a list of tuples

data = [('John', 25), ('Jane', 22), ('Dave', 30)]
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
print(sorted_data)  # Output: [('Dave', 30), ('John', 25), ('Jane', 22)]



# 3. Filtering a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

all_numbers = list(filter(lambda x: x > 5, numbers))

print(all_numbers)  # Output: [6, 7, 8, 9, 10]