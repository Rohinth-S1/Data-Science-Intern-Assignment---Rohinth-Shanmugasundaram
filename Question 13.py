"""
Find how many pairs in a binary number that starts and ends with 1
Expected Input 1:
100101
Expected Output:
2
Expected Input 2:
1001101010010
Expected Output:
15

"""

def count_pairs(binary_str):
    count_ones = binary_str.count('1')
    return count_ones * (count_ones - 1) // 2


input1 = "100101"
print("Output for Input 1:", count_pairs(input1))
input2 = "1001101010010"
print("Output for Input 2:", count_pairs(input2))

"""
- Here as it is combination and not permutation as the value given is fixed and not rearranged
- Combinational formula - n*(n-1)//2 
"""