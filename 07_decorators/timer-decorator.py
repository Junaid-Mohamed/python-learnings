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
    
example_function(4)