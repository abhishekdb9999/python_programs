def simple_password_checker(password):
    # Check if the password meets basic criteria
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
    elif not any(char in "!@#$%^&*()" for char in password):
        print("Password must contain at least one special character.")
    else:
        print("Password is valid!")

# Test the simple password checker
password = input("Enter a password to check: ")
print(simple_password_checker(password))

