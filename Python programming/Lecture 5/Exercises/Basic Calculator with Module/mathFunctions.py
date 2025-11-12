def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


module_name = "Simple Math Functions Module"

if __name__ == "__main__":
    print("This module starts with mathFunction.py")
else:
    print("mathFunctions.py module has been imported")