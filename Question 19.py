"""Question 19:

Cyclic rotation:

Case 1: first element moves to last and rest all the elements move one step to left
Case 2: last element moves to first and rest all the element move  one step to right

Input 1 Description: 1 - first to last  2- last to first
Input 2 Description : string
Input 3 Description : no of times
Expected Input 1:
1
'happy'
2
Expected Output:
Appyh
ppyha
Expected Input 2:
2
'happy'
3
Expected Output:
yhapp
pyhap
"""
def cyclic_rotation(case, s, n):
    for _ in range(n):
        if case == 1:
            s = s[1:] + s[0]
        elif case == 2:
            s = s[-1] + s[:-1]
        print(s)

print("Expected Output for Input 1:")
cyclic_rotation(1, 'happy', 2)

print("\nExpected Output for Input 2:")
cyclic_rotation(2, 'happy', 3)

"""
- Here to achieve this cases 
- 1. first value is called last and remaining values are called first
- 2. Last value is called first and the remaining values are called afterwards
"""