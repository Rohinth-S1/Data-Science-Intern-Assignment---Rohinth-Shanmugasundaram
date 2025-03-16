"""Question 3:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Expected Input:
hello world and practice makes perfect and hello world again
Expected Output:
again and hello makes perfect practice world
Note:
In case of taking data from the user, it should be in a comma-separated form.
"""

a = input("please enter sequence of words seperated by space: ")
b = a.split(" ")
c = set(b)
d = sorted(c)
output = " ".join(d)
print(output)

"""
- Here the input has spaced sequence of word, which is splited by space
- set function is passed to remove duplicates, sorted and joined with space
"""