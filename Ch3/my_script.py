"""
Writing and Executing Our First Script
"""

import math

numbers = [5, 7, 11]

result = sum([math.factorial(n) for n in numbers])
print(result)
