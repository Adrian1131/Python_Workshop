'''
Using Bubble Sort in Python
'''

# time complexity = O(N^2)

# start with a list of numbers
l = [5,8,1,3,2]

# create an indicator that will tell us when you can stop looping through the array
still_swapping = True

# look through each number and compare it to the maximum
while still_swapping:
    still_swapping = False
    # for loop
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
            still_swapping = True
            print(l)
