# Lab 2: Map, Filter, Reduce
# Reference: CSC3301

from functools import reduce 

# SAmple data
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Map - transform each elemnt (doubled)
doubled = list(map(lambda x: x * 2,nums))
print("Doubled", doubled)

# Filter - filter out even numbers
evens = list(filter(lambda x: x%2 == 0, nums))
print("Evens", evens)

# Reduce - sum of all numbers
total = reduce(lambda a, b: a + b, nums)
print("Total", total)


# Pipeline: filter -> map -> reduce
result = sum(x ** 2 for x in nums if x % 2 == 0)
print("Sum of squares of evens", result)
