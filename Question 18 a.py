"""
Question 18:
Solve the following patterns

Input Description:   row count

Expected Input:
 4
Expected Output:

1
2 * 3
4 * 5 * 6
7 * 8 * 9 * 10
"""
def pattern1(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" * ".join(row))

pattern1(4)

"""
- Here number of column is increased every time by one thar is by j
- Here i is a arithmetic operation increased by 1
"""