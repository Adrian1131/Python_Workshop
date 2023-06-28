#set variable for while loop
i = 1 
#while loop starts, ends at 10.
while i <= 10:
    print(i)
    i += 1

#infinite loop
x = 5 
while x <= 10:
    print(x)
    break

#Find the first number greater than 100 and divisible by 17
x = 100 
while x <= 1000:
    x += 1 #allows the loop to start at 101
    if x % 17 == 0:
        print('', x, 'is the first number greater than 100 that is divisible by 17.')
    