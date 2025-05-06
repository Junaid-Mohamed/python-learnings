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