'''
Binary Search in Python
'''

# create a new list of numbers
l = [2, 3, 5, 8, 11, 12, 18]

# specify the value to search for
search_for = 11

# create two variable that will represent the start and end locations.
slice_start = 0
slice_end = len(l) - 1

# add a variable to ensure the search was successful
found = False

# find the midpoint, check if the value is greater than or less than the search term
while slice_start <= slice_end and not found:
    location = (slice_start + slice_end) // 2
    if l[location] == search_for:
        found = True
    else:
        if search_for < l[location]:
            slice_end = location - 1
        else:
            slice_start = location + 1

            print(found)
            print(location)

