def divide(x, y):
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("An unexpected error occurred:", str(e))