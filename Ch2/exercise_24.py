"""
Implementing Matrix Operations (Multiplication)
"""
# initialize nested lists
x = [[1, 2], [4, 5], [3, 6]]
y = [[1,2,3,4], [5,6,7,8]]
# zero matrix placeholder
result = [[0,0,0,0], [0,0,0,0],[0,0,0,0]]
# iterating by row of x
for i in range(len(x)):
    # iterating by column of y
    for j in range(len(y[0])):
        # iterating by rows of y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for r in result:
    print(r)
