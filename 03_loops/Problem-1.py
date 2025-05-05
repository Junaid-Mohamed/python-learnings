"""
count positive numbers.
"""

nums = [1,2,-3,-4,5,-6,-7,-8]
positiveNumCount = 0
for num in nums:
    if num > 0:
        positiveNumCount += 1

print(positiveNumCount)