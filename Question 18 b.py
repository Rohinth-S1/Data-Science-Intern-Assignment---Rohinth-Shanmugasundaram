"""
Input Description:   row count

Expected Input:
4
Expected Output:

      *
    *  *
   * * *
  * * * *
   * * *
    *  *
      *


"""
def pattern2(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

pattern2(4)

"""
- Here as the star formation is symmetric
- both positive and negative indexing have similar factor of operation
"""
