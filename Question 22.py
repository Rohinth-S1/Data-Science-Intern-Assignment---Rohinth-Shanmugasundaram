"""
Question 22:
Convert Decimal to binary (Without inbuilt function)
Expected Input 1:
12
Expected Output:
1100
Expected Input 2:
20
Expected Output :
10100

"""
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary


decimal_number1 = 12
print(f"Binary of {decimal_number1}: {decimal_to_binary(decimal_number1)}")

decimal_number2 = 20
print(f"Binary of {decimal_number2}: {decimal_to_binary(decimal_number2)}")

"""
- Here the operation works under the logic that, a numbers is divided by 2 until
  it is equivalent to zero "0"
- the remainders are stacked together from backwards to form a binary number
"""