age = 20
if age >= 20 and age < 21:
    print('Atleast you can vote.')
    print('Poker will have to wait. \n\n\n')

#using nested conditionals
if age >= 18:
    print('You can vote.')
    if age >= 21:
        print('You can play poker.')

#if else syntax
if age < 18:
    print('You aren\'t old enough to vote.')
else:
    print('Welcome to our voting program.')

if age >= 18:
    print('Welcome to the voting program..')
else:
    print('Sorry, you are not old enough to vote.')