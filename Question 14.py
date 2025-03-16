"""
Question 14:
Find the minimum possible denominations for given valid currency.
(No of currencies used should be minimum)
Expected Input 1:
valid_currency: [1,2,5,10,20,50,100,200,500,2000]
Money: 210
Expected Output:
200-1
10-1
Expected Input 2:
valid_currency: [1,2,5,10,20,50,100,200,500]
Money: 556
Expected Output:
500-1
50-1
5-1
1-1
Expected Input 3:
valid_currency: [1,2,5,10,20,50,100,200,500,2000]
Money: 2000
Expected Output:
2000-1
Expected Input 4:
valid_currency: [1,2,5,10,20,50,100,500,1000]
Money: 210
Expected Output:
100-2
10-1
Expected Input 5:
valid_currency: [1,2,5,10,20,50,100,200,500,1000]
Money: 2000
Expected Output:
1000-2

"""

def minimum_denominations(valid_currency, money):
    valid_currency.sort(reverse=True)


    result = {}

    for currency in valid_currency:
        if money >= currency:
            count = money // currency
            result[currency] = count
            money -= count * currency

    for currency, count in result.items():
        print(f"{currency}-{count}")



valid_currency1 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
money1 = 210
print("Output for Input 1:")
minimum_denominations(valid_currency1, money1)

valid_currency2 = [1, 2, 5, 10, 20, 50, 100, 200, 500]
money2 = 556
print("\nOutput for Input 2:")
minimum_denominations(valid_currency2, money2)

valid_currency3 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
money3 = 2000
print("\nOutput for Input 3:")
minimum_denominations(valid_currency3, money3)

valid_currency4 = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
money4 = 210
print("\nOutput for Input 4:")
minimum_denominations(valid_currency4, money4)

valid_currency5 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
money5 = 2000
print("\nOutput for Input 5:")
minimum_denominations(valid_currency5, money5)

"""
- Here is the the currencies are decending ordered and checked id they are greater 
  than money required, if so modulus is taken to know the count
- if not passed to other currency unless the value becomes zero
"""