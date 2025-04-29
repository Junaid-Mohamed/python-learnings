"""
Password checker

based on number of char's

"""

password = "Secure3P@ass"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else: 
    strength = "Strong"

print("Password strength is ", strength) 