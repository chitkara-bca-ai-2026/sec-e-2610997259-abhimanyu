
username = input("Enter your username: ")
password = input("Enter your password: ")

has_min_length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

print("PASSWORD VALIDATION REPORT")

print(f"Username: {username}")
print(f"Password: {'*' * len(password)}\n")

print("--- Validation Rules ---")
length_status = "[PASS]" if has_min_length else "[FAIL]"
digit_status = "[PASS]" if has_digit else "[FAIL]"
upper_status = "[PASS]" if has_upper else "[FAIL]"

print(f"{length_status} Minimum 8 characters ({len(password)} characters)")
print(f"{digit_status} At least one digit")
print(f"{upper_status} At least one uppercase letter\n")

print("--- Result ---")
if has_min_length and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!\n")
else:
    print("Password is INVALID!\n")