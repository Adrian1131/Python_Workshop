"""
Prompt the user to bid on a house and let them
know it when the bid has been accepted
"""
print('A one bedroom in the Bay Area is listed at $599,000.')
print('====================================================')
print('Enter your first offer on the house: ')
offer = abs(int(input()))

print('Enter your best offer on the house: ')
best = abs(int(input()))

print('How much more do you want to offer each time? ')
increment = abs(int(input()))

offer_accepted = False

while offer <= best:
    if offer >= 650000:
        offer_accepted = True
        print('Your offer of', offer, 'has been accepted!')
        break
    else:
        print('We\'re sorry, you\'re offer of', offer, 'was not accepted.')
        offer += increment