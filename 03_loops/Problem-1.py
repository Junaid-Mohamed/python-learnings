"""
count positive numbers.
"""

nums = [1,2,-3,-4,5,-6,-7,-8]
positiveNumCount = 0
for num in nums:
    if num > 0:
        positiveNumCount += 1

print(positiveNumCount)

"""
sum of even numbers
"""

n = 10
sum = 0

for i in range(n+1):
    if i%2==0 :
        sum +=i

print('Sum of even numbers till {n} {sum}'.format(n=n,sum=sum))

"""
Reverse a str using for loop
"""

string = "Python"
reversedString = ""
for char in string:
    reversedString = char + reversedString

print(reversedString)

"""
find 1st non-repeated char
"""

str = "tetedrd"

# r should be the ans.

for char in str:
    if str.count(char) == 1:
        print(char)
        break

"""factorial using while loop"""

number = 5
factorial = 1

while number > 0 :
    factorial*=number
    number -= 1

print("Factorail of 5 is",factorial)

"""
input validation
"""

while True:
    numberInput = int(input("Enter a num b/w 1 and 10: "))
    if 1 <= numberInput <= 10:
        print("Thanks!")
        break
    else:
        print("Invalid input try again!!")