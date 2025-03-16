"""
Input Description:   row count (only odd)
Expected Input:
5
Expected Output:

1 1 1 1 1
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
1 1 1 1 1


"""

def pattern5(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("1 " * n)
        else:
            print("0 " * (n // 2) + "1 " + "0 " * (n // 2))
pattern5(5)

"""
- The spaces are calculated numbered and the similar stars are paired in similar 
  comditonal statements to arrive at the pattern
"""