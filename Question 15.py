"""
Question 15:
There is a bus travelling from Town A to Town B. There are n stops between them and bus has to make m stops.
Find the numbery of ways in the travel so that no stop is consecutive
Expected Input 1:
n=12
m=4
Expected Output:
Output :126
Expected Input 2:
n = 16
s = 5
Expected Output:
792

"""

import math

def number_of_ways(n, m):
    return math.comb(n - m + 1, m)


n1, m1 = 12, 4
print("Output for Input 1:", number_of_ways(n1, m1))

n2, m2 = 16, 5
print("Output for Input 2:", number_of_ways(n2, m2))

"""
- Here we are seeking selection of stops without consecutiveness
- combination of (n-m+1, m ) is used so that the gap between n stops and m stops are factored
  in on all possible combinations
"""