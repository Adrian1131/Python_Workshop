"""
Using the zip() Method to Manipulate Dictionaries
"""
items = ['apple', 'orange', 'banana']
quantity = [5,3,2]

orders = zip(items, quantity)
print(orders)

# turning zipped object into a list
orders = zip(items, quantity)
print(list(orders))

