def password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    else:
        return "Weak"

pwd = input("Enter password: ")
print(password_strength(pwd))