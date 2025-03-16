"""
Question 21:
Check whether the given number is Armstrong number or not
Armstrong number: 153 => 1^3+5^3+3^3=153 (If summing each digit to the power of number of digits results to the same number then it is a Armstrong number)

1634 => 1^4+6^4+3^4+4^4 =1634         1^4 => digit^(number of digits)
Expected Input:
1634
Expected Output:
 Armstrong number

"""
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

"""
- The unique feature here the the number is first converted to string 
  so that its length is determined
- Just about when it is to be raised - its turned back to integer
"""