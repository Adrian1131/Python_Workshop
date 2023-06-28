"""
Using a nested list to store employee data
"""

employees = [['Adrian Jones', 54, 'Engineering'], ['Tom Benshon', 23, 'Accounting'], ['Unbentu Kolie', 36, 'HR']]
print(employees)

for employees in employees:
    print('Name: ', employees[0])
    print('Age: ', employees[1])
    print('Department:', employees[2])
    print('-' * 20)
