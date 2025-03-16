"""
Program to print the pattern ‘G’
Input Description : No of rows

Expected Input:
7
Expected Output:

  ***
 *
 *
 * ***
 *      *
 *      *
  * * *

"""
def pattern4(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print(" " * (n // 2) + "*" * (n // 2))
        elif i == n // 2:
            print("*" + " " * (n // 2 - 1) + "*" * (n // 2))
        else:
            print("*" + " " * (n - 2) + "*")
pattern4(7)

"""
- The spaces are calculated numbered and the similar stars are paired in similar 
  comditonal statements to arrive at the pattern
"""