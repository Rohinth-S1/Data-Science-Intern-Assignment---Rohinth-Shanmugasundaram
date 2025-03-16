"""
Find whether the given number is perfect number or not.
Any number can be perfect number in Python, if the sum of its positive divisors excluding the number itself is equal to that number.

For example, 6 is a perfect number in Python because 6 is divisible by 1, 2, 3 and 6.
So, the sum of these values are: 1+2+3 = 6 (Remember, we have to exclude the number itself.
That’s why we haven’t added 6 here). Some of the perfect numbers are 6, 28, 496, 8128 and 33550336 so on.
Expected Input:
28
Expected Output:
Perfect number
"""

def is_perfect_number(n):
    if n <= 1:
        return False


    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

"""
- For the range from 1 to n//2 the numbers are checked for perfect divisibility 
  with remainder zero
- These numbers are checked for their sum is the number itself - to be acknowleged as
  perfect number
"""