"""
Question 12:
Find the pair of alphabets in an alphanumeric string whose sum of numbers in between is always 9
Expected Input 1:
a54b12c
Expected Output:
a,b
Expected Input 2:
a55b234cd9f63de54x3m
Expected Output:
b,c
b,d
d,f
f,d
f,e
e,x

"""
def find_pairs_with_sum_9(sequence):
    pairs = []
    n = len(sequence)

    for i in range(n):
        if sequence[i].isalpha():
            for j in range(i + 1, n):
                if sequence[j].isalpha():
                    substring = sequence[i + 1:j]
                    digits = [char for char in substring if char.isdigit()]
                    # Calculate the sum of digits
                    total = sum(int(char) for char in digits)
                    if total == 9:
                        pairs.append((sequence[i], sequence[j]))
    for pair in pairs:
        print(f"{pair[0]},{pair[1]}")

input1 = "a54b12c"
print("Output for Input 1:")
find_pairs_with_sum_9(input1)

input2 = "a55b234cd9f63de54x3m"
print("\nOutput for Input 2:")
find_pairs_with_sum_9(input2)

"""
- Here the alphabets in the sequence are identified
- every char between them are sub stringed 
- and the the intergers between them are added to verify value 9
- But, I think we are missing an important condition in our question,
because c,f - which is not in the expected out also has 9 as well as dx, or I migth be wrong.
"""