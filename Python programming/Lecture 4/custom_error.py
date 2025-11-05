class CustomError(Exception):
    
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        
    def __str__(self):
        if self.error_code:
            return f"[Error {self.error_code}]: {self.message}"
        return f"CustomError: {self.message}"


class ValidationError(CustomError):
    
    def __init__(self, message, field_name=None):
        super().__init__(message, error_code="VAL001")
        self.field_name = field_name
        
    def __str__(self):
        if self.field_name:
            return f"[Validation Error] {self.field_name}: {self.message}"
        return f"[Validation Error]: {self.message}"


class DatabaseError(CustomError):
    
    def __init__(self, message, query=None):
        super().__init__(message, error_code="DB001")
        self.query = query
        
    def __str__(self):
        base_msg = f"[Database Error]: {self.message}"
        if self.query:
            return f"{base_msg}\nQuery: {self.query}"
        return base_msg


class AuthenticationError(CustomError):
    
    def __init__(self, message, username=None):
        super().__init__(message, error_code="AUTH001")
        self.username = username
        
    def __str__(self):
        if self.username:
            return f"[Authentication Error] User '{self.username}': {self.message}"
        return f"[Authentication Error]: {self.message}"


class FileProcessingError(CustomError):
    
    def __init__(self, message, file_path=None):
        super().__init__(message, error_code="FILE001")
        self.file_path = file_path
        
    def __str__(self):
        if self.file_path:
            return f"[File Processing Error] {self.file_path}: {self.message}"
        return f"[File Processing Error]: {self.message}"


if __name__ == "__main__":
    
    try:
        raise ValidationError("Age must be between 0 and 120", field_name="age")
    except ValidationError as e:
        print(e)
    
    try:
        raise DatabaseError("Connection timeout", query="SELECT * FROM users")
    except DatabaseError as e:
        print(e)
    
    try:
        raise AuthenticationError("Invalid credentials", username="john_doe")
    except AuthenticationError as e:
        print(e)
    
    try:
        raise FileProcessingError("File not found", file_path="/path/to/file.txt")
    except FileProcessingError as e:
        print(e)
    
    try:
        raise CustomError("Something went wrong", error_code="GEN001")
    except CustomError as e:
        print(e) 
