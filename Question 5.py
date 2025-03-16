"""
Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Expected Input:
hello world! 123
Expected Output:
LETTERS 10
DIGITS 3
Note:
In case of taking data from the user, it should be in a comma-separated form.

"""


a = input("please enter your sequence: ")


def letters_digits(sequence):
    Letters = 0
    Digits = 0
    for char in sequence:
        if char.isalpha():
            Letters += 1
        elif char.isdigit():
            Digits += 1
    return Letters, Digits

Letters, Digits = letters_digits(a)

print(f"LETTERS {Letters}")
print(f"DIGITS {Digits}")

""" 
- Here I have created a function so that each character is checked for its data type 
- For each letters and digits its respective variable is added with one and retured in the output
"""

