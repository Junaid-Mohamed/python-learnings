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