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

# def sum(n1,n2):
#     return n1+n2

# sumOfNums = sum(5,2)
# print(sumOfNums)

"""
function that numtiplies nums or str
ploymorphism
"""

def multiply(p1,p2):
    return p1*p2

print(multiply(2,4))
print(multiply(2,'a'))
print(multiply('b',4))

"""
circle stats
area of circle = pi*r*r
circumference of circle = 2 * pi * r
"""

import math

def circleStats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area,2), round(circumference,3)

a , c = circleStats(2)

print("Area ",a," circumference", c)

"""
lambda function
mainly used in frameworks
usually used for 1 time
"""

result = lambda x : x ** 3
print(result(3))

"""
function with *args
this comes in as tuple
"""

def summ(*args):
    return sum(args)

print(summ(2,3,4))
print(summ(2,3,4,5))

"""
function with *kwargs
this  comes in as dict
"""

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="Junaid")
print_kwargs(name="Junaid", age=30)
print_kwargs(name="Junaid", city="Bangalore")

"""
generator function
"""

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

val = even_generator(10)
print(val.__next__())
print(val.__next__())
print(val.__next__())
print(val.__next__())
print(val.__next__())
print(val.__next__())

"""
factorial
"""

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(5))