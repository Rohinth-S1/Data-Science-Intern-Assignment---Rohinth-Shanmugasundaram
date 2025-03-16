"""
Question 9:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
Expected Input:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Expected Output:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""


tuples = []
print("Enter tuples in the format 'name,age,height'. Type 'done' to finish:")
while True:
    user_input = input().strip()
    if user_input.lower() == 'done':
        break
    try:
        name, age, height = user_input.split(',')
        age = int(age)
        height = int(score)
        tuples.append((name, age, score))
    except ValueError:
        print("Invalid input format. Please enter in the format 'name,age,height'.")
tuples.sort(key=lambda x: (x[0], x[1], x[2]))
print("Sorted Tuples:")
print(tuples)

"""
- Here each line is accepted as seperate item with the help of strip(), and if = done
- As it is the list of items, the input is taken in each line instead of being comma seperated
- age and score are converted to integer
- they are sorted in the order of name, age and score
- they are returned as a list of tuples
"""