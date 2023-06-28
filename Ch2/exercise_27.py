"""
Adding Items to Our Shopping List
"""
# using the append method
shopping = ['bread', 'milk', 'eggs']
shopping.append('apple')
print(shopping)

# adding items one by one to an empty list
shopping = []
shopping.append('bread')
shopping.append('milk')
shopping.append('eggs')
shopping.append('apple')
shopping.append('orange')
print(shopping)

# insert method
shopping.insert(2, 'ham')
print(shopping)
