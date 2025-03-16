"""Question 4:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Note:
 In case of taking data from the user, it should be in a comma-separated form.
"""
even_number = []

for i in range (1000, 3001):
    if i%2 == 0:
        even_number.append(str(i))
        output = ",".join(even_number)
print(output)

""" 
-Here remainder function is called to confirm even numbers
-converted to string and joined with comma
"""