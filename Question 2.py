"""
Question 2:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Expected Input:
without,hello,bag,world
Expected Output:
bag,hello,without,world
Note:
 In case of taking data from the user, it should be in a comma-separated form.

"""
a = input("Please enter the words seperated by comma: ")
b = a.split(",")
c= sorted(b)
output = ",".join(c)
print(output)

""" Here the inmput is splited by comma, sorted and joined by comma to arrive at the output"""