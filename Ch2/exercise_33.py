"""
Implementing Set Operations
"""

s5 = {1,2,3,4}
s6 = {3,4,5,6}

print(s5 | s6)
print(s5.union(s6))
print('-' * 20)

print(s5 & s6)
print(s5.intersection(s6))
print('-' * 20)

print(s5 - s6)
print(s5.difference(s6))
print('-' * 20)

print(s5 <= s6)
print(s5.issubset(s6))
print('-' * 20)

s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))
print(s7 < s8)
print('-' * 20)

s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 < s9)
print('-' * 20)

print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)
print('-' * 20)
