"""
Question 6:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Expected Input:
Hello world!
Expected Output:
UPPER CASE 1
LOWER CASE 9
Note:
 In case of taking data from the user, it should be in a comma-separated form.

"""
a = input("please enter your sequence: ")


def Case_detector (sequence):
    UPPER_CASE = 0
    LOWER_CASE = 0
    for char in sequence:
        if char.isupper():
            UPPER_CASE += 1
        elif char.islower():
            LOWER_CASE += 1
    return UPPER_CASE, LOWER_CASE

UPPER_CASE, LOWER_CASE = Case_detector(a)

print(f"UPPER CASE {UPPER_CASE}")
print(f"LOWER CASE {LOWER_CASE}")

"""
- Here I have created a function so that each character is checked for its case
- For each (Upper or Lower Case Detection) its respective variable is added with one and retured in the output
"""