"""
timing function decorator
to print the time taken of each function
"""

import time

def timer(func):
     def wrapper(*args,**kwargs):
          start = time.time()
          result = func(*args,**kwargs)
          end = time.time()
          print(f"{func.__name__} took {end-start} time to exec")
          return result
     return wrapper

@timer
def example_function(n):
     time.sleep(n)
    
# example_function(4)

"""
Problem 2
Debugging function calls
decorator to print the function name and the values of its args every time the func is called
"""

def debugger(func):
     def wrapper(*args,**kwargs):
          result = func(*args, **kwargs)
          print(f"function {func.__name__} is called with following params")
          if(args):
               print(args)
          if(kwargs):
               print(kwargs)
          return result
     return wrapper

@debugger
def example_function2(a,b, c="junaid"):
     print(f"this is a function with {a}, {b}, {c} params")

example_function2(2,3,c="Suhail")

"""
cache return values
Implement a decorator that cahces the return values of a function, so that when it's called with the same arguments, the cached value is returnd instead of 
re-executing the function
"""


def cache(func):
     cache_value = {}
     def wrapper(*args):
          print(f"{cache_value} is in cache")
          if args in cache_value:
               return cache_value[args]
          result = func(*args)
          cache_value[args] = result
          return result
     return wrapper

@cache
def long_running_func(a,b):
     time.sleep(2)
     return a+b

print(long_running_func(2,3))
print(long_running_func(2,3))
print(long_running_func(4,3))
