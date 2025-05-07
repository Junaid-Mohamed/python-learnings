"""
basic function syntax
ex. square of a number
"""

def sqaure(n):
    return n ** 2

num = sqaure(4)
print(num)

""""
function take 2 nums and returns a sum
"""

def sum(n1,n2):
    return n1+n2

sumOfNums = sum(5,2)
print(sumOfNums)

"""
function that numtiplies nums or str
ploymorphism
"""

def multiply(p1,p2):
    return p1*p2

print(multiply(2,4))
print(multiply(2,'a'))
print(multiply('b',4))