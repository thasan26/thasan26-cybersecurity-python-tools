import re

def check_password_strength(password):
    
    score = 0
    
    if len(password) >= 8:
        score += 1
        
    if re.search("[A-Z]", password):
        score += 1
        
    if re.search("[a-z]", password):
        score += 1
        
    if re.search("[0-9]", password):
        score += 1
        
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        return "Strong Password"
    elif score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"


password = input("Enter a password: ")
strength = check_password_strength(password)

print("Password Strength:", strength)