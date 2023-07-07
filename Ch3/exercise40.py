'''
Linear Search in Python
'''

# time complexity: O(n)

# start a new list
l = [5, 8, 1, 3, 2]

# specify a value for our search
search_for = 8

# create a result variable that has a default of -1, if search is unsuccessful it will stay at -1 once the algorithm
# is executed
result = -1

# Loop through the list. If the value equals the search value, set the result, and exit the loop.
for i in range(len(l)):
    if search_for == l[i]:
        result = i
        break

print(result)
