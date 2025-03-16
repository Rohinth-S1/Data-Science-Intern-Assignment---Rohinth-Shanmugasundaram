"""
Question 8:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-`9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Passwords that match the criteria are to be printed, each separated by a comma.
Expected Input:
ABd1234@1,a F1#,2w3E*,2We3345
Expected Output:
ABd1234@1
Note:
In case of taking data from the user, it should be in a comma-separated form.

"""
from operator import truediv


def is_valid_password(password):
    if not 6<= len(password) <= 12:
        return False
    has_lower = any(char.islower() for char in password )
    if not has_lower:
        return False
    has_upper = any(char.isupper() for char in password )
    if not has_upper:
        return False
    special_char = {'#', '@','$' }
    has_special = any(char in special_char for char in password )
    if not has_special:
        return False
    return True

passwords_input = input("type in valid passwords with a upper, lower, interger and a special: ")
passwords = passwords_input.split(',')

valid_password = []
for password in passwords:
    stripped_password = password.strip()
    if is_valid_password(stripped_password):
        valid_password.append(stripped_password)

print(",".join(valid_password))


"""
- Here if not function is used to stop the passwords that doesn't qualify
- if the remaining passwords have spaces, they are stripped and returned
"""