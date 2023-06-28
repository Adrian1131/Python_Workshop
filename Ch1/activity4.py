# initialize
x = 24
y = 36
# make counting be a boolean for loop
counting = True

# set our increment
i = 1
# start of loop
while counting:
    if i % x == 0 and i % y == 0:
        i += 1
        # prints result.
    print('The least common multiple of', x, ' and ', y, ' is ', i, '.')
    break
    # breaks and ends loop.
    # could not get the right result.
