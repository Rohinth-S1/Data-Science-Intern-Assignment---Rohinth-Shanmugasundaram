"""
Input Description:   row count

Expected Input:
4
Expected Output:

1
2 * 3
4 * 5 * 6
7 * 8 * 9 * 10
4 * 5 * 6
2 * 3
1
"""
def pattern3(n):
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" * ".join(row))
    num = num - n
    for i in range(n - 1, 0, -1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" * ".join(row))
        num = num - 2 * i + 1
pattern3(4)

"""
- It is similar to the last example - but there the spaces came first
- here numbers come first, which is processed as the same way as the stars
"""