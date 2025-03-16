"""
Question 10:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The numbers after the direction are steps.
The trace of robot movement is shown as the following:
Expected Input:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Expected Output:
Compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Note:
In case of taking data from the user, it should be in a comma-separated form.

"""
import math
x, y = 0, 0

print("Enter robot movements in the format 'DIRECTION STEPS', separated by commas:")
user_input = input().strip()
movements = user_input.split(',')

for movement in movements:
    try:
        direction, steps = movement.strip().split()
        steps = int(steps)

        if direction.upper() == 'UP':
            y += steps
        elif direction.upper() == 'DOWN':
            y -= steps
        elif direction.upper() == 'LEFT':
            x -= steps
        elif direction.upper() == 'RIGHT':
            x += steps
        else:
            print(f"Invalid direction: {direction}. Skipping this movement.")
    except ValueError:
        print(f"Invalid input format: {movement}. Please enter in the format 'DIRECTION STEPS'.")


distance = math.sqrt(x**2 + y**2)
distance = round(distance)
print(f"Distance from origin: {distance}")

"""
- Here the values of up and down are inputed to the same arithmetic variable
- the same is done for left and right
- they are calculated for sqrt(x**2 + y**2) as origin is (0,0)
- and distance from origin is calculated
"""