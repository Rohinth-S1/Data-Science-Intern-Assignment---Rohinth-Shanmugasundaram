"""
Question 17:
Validate Email Address:
a. Check for '@' symbol, it should be only 1
b. Only lower-case letters are allowed
c. Numbers are allowed
e. No symbols allowed other than '.' & '_'
"""

email = input("type any email here: ")


def validate_email(email):
    if email.count('@') != 1:
        return False


    local_part, domain_part = email.split('@')

    for char in local_part:
        if not (char.islower() or char.isdigit() or char in ['.', '_']):
            return False

    for char in domain_part:
        if not (char.islower() or char.isdigit() or char == '.'):
            return False
    if '.' not in domain_part:
        return False
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False

    return True

result = validate_email(email)
print(result)

"""
- Here more conditions can be inputed on the .com or .in or other extentions
- but there are so many extentions to consider that
- if there is a specific pourpose - like a company may use similar extentions throughout, in that 
  case it would be easy
"""