def divide(x, y):
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
    
    
def divicde_by_try(x, y):
    try:
        result = x / y
        
    except TypeError:
        return "Error: Invalid input types."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    else:
        return result
    
    
class BankAccount:
    def __init__(self, account_holder, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder = account_holder
        self.balance = balance 
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance
    
try: 
    acc = BankAccount("Jane Doe", -500)
    print(f"Initial balance: {acc.balance}")
    print(f"Balance after deposit of 200: {acc.deposit(200)}")
    print(f"Balance after withdrawal of 800: {acc.withdraw(-500)}")
except ValueError as ve:
    print("Transaction error:", str(ve))