"""
Age group categorization.
below 13 -> child
teenager -> 13 - 19
adult -> 20 - 59
Sennior -> 60+
"""

user_age = int(input("Enter you age: "))

if(user_age < 13):
    print("Your a child.")
elif(user_age < 20):
    print("Your a teenager.")
elif(user_age < 60):
    print("Your an adult.")
else:
    print("Your a Senior")