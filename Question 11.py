"""
Question 11:
Find the continuous occurrence of the string.
Expected Input:
Aabbcdeefffaabbcc
Expected Output:
a2b2c1d1e2f3a2b2c2

"""

sequence = input("print you sequence here: ")

def continuous_occurrence(sequence):
    sequence = sequence.casefold()
    result = ""
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            result += sequence[i - 1] + str(count)
            count = 1
    result += sequence[-1] + str(count)
    return result

output = continuous_occurrence(sequence)
print(output)

"""
- Here sequence is made casefold to make case insensitive
- and for every recurrance the count is incremented
- at last at the end  - the lase character and its count is added to arrive at the output.
"""