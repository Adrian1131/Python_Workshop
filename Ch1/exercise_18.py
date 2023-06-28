"""
Write a program to check to see whether the users number is a perfect square.

"""
# prompts user with message
print('Enter a number to see if it\'s a perfect square: ')

# set variables
number = input()
number = abs(int(number))

# set iterator variable
i = -1
# initialize boolean
square = False

# start of while loop.
while i <= number ** 0.5:
    i += 1
    if i * i == number:
        square = True
        break
    if square:
        print('The square root of', number, 'is', i, '.')
    else:
        print('', number, 'is not a perfect square.')

        break
