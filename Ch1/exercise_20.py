"""
For loops
"""

for i in 'Portland':
    print(i)


for i in range(1, 10):
    print(i)


# using a step increment
for i in range(1, 11, 2):
    print(i)

# using a step increment to count down
for i in range(3, 0, -1):
    print(i)


# nested loops
name = 'Adrian'
for i in range(3):
    for i in name:
        print(i)

# the following code prints out every two digit prime number.
for num in range(10, 100):
    if num % 2 == 0:
        continue
    if num % 3 == 0:
        continue
    if num % 5 == 0:
        continue
    if num % 7 == 0:
        print(num)