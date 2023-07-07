"""
Accessing a Dictionary Using Dictionary Methods
"""

orders = {'apple': 5, 'orange': 3, 'banana': 2}
print(orders.values())
print(list(orders.values()))

# using keys method
print(list(orders.keys()))

# converting to a list since you can not directly iterate a dictionary
for tuple in list(orders.items()):
    print(tuple)
    