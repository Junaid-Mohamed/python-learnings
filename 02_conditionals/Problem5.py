"""
leap year
"""

year = 2028

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("Not leap year")