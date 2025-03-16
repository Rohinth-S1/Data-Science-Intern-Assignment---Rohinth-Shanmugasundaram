""" Question 1:

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Expected Input:
3,5
Expected Output:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
input_xy = input("please enter two numbers seperated by comma: ")
a = input_xy.split(",")
x = int(a[0])
y = int(a[1])

array = [[i * j for j in range(y)] for i in range(x)]

print(array)

"""Here j from y is called first - to populate list of 5 and i from x is called to create 3 lists of 5 items"""
