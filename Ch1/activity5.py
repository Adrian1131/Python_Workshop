"""
Building Conversational Bots using Python.
"""

print('What is your name?')

name = input()
print('Great.', name, "is my name too.")

print('Have you thought about programming today?')
yes_no = input()

print('I am so glad you said', yes_no, '. I was thinking something similar.')

print('We\'re people you may have not known of ', name, '.')

print('How intelligent are you, 1 - 10, give a rating.')
rating = input()
rating = int(rating)

if rating <= 3:
    print('Are you sure?')
    print('How bad of a day of are you having give a rating of 1 - 10 also.')

    day = input()
    day = int(day)

    if day <= 5:
        print('I can try to help. All I can say.')
    else:
        print('You seem to have a proper approach.')
elif rating <= 6:
    print('You are probably a lot smarter than you think.')

    print('How much time do you tend to spend online?')
    hours = input()
    hours = int(hours)
    if hours <= 4:
        print('You don\'t think that can be a potential issue?')
    else:
        print('And I thought it was only me feeling similar.')

elif rating <= 8:
    print('Are you human by change? Wait. Don\t answer that.')
    print('How human are you on a scale of 1 - 10?')
    human = input()
    human = int(human)
    if human <= 5:
        print('I knew it.')
    else:
        print('I think this is over.')
else:
    print('I see.. how many operating systems can you run?')
    os = int
    os = int(os)

    if os <= 2:
        print('Good thing you\'re taking advantage of it for school.')
    else:
        print('What is this? A competition?')

