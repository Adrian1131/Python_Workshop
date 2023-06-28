"""
Storing Company Employee Table Data Using a List and a Dictionary
"""

employees = [
    {'name': 'John Mckee', 'age': 38, 'Department': 'Sales'},
    {'name': 'Lisa Crawford', 'age': 29, 'Department': 'Marketing'},
    {'name': 'Sujan Patel', 'age': 33, 'Department': 'HR'}

]
print(employees)

# using a for loop
for employee in employees:
    print('Name:', employee['name'])
    print('Age:', employee['age'])
    print('Department:', employee['Department'])
    print('-' * 20)
    
