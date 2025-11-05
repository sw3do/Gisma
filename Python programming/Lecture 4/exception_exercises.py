def multiple_exception_types(data):
    try:
        func_data = [10, 20, 30, 40]
        return func_data[data]
    except IndexError:
        return "Error: Index out of range."
    except TypeError:
        return "Error: Invalid input type."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


x_data = [10, 20, 30, 40]
print(multiple_exception_types(2))      # Valid index
print(multiple_exception_types(10))     # IndexError
print(multiple_exception_types('a'))    # TypeError
print(multiple_exception_types(None))   # TypeError


class CustomError(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        
    def __str__(self):
        if self.error_code:
            return f"[Error {self.error_code}]: {self.message}"
        return f"CustomError: {self.message}"
    

def show_error():
    try:
        raise CustomError("This is a custom error message.", error_code=1001)
    except CustomError as ce:
        print(ce)
        
        
show_error()

def file_handling(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: An I/O error occurred while handling the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        
file_handling("non_existent_file.txt")
file_handling("existing_file.txt")


def try_except_else_in():
 while True:
    try:
        num = int(input("Enter a number to divide 100 by: "))
        result = 100 / num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        break
    else:
       return print(f"Result: {result}")
    
try_except_else_in()