"""
Implementing Matrix Operations (Addition and subtraction)
"""

# initialize nested lists, store values
x = [[1,2,3], [4,5,6], [7,8,9]]
y = [[10,11,12], [13,14,15], [16,17,18]]

# intialize a result placeholder
result = [[0,0,0],[0,0,0],[0,0,0]]

# iterate through rows
for i in range(len(x)):
# iterate through the columns
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

print(result)
