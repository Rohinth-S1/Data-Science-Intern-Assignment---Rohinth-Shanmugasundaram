"""
Question 20:
In a pathology lab test, there are n number of samples for testing the health condition of a patient,
each slide has 5 components, Sugar level, Blood pressure, Heartbeat rate, weight and fat percentage,
based on input as provided by the patient's blood report.

1. Create a sample input for a healthy patient as follows:

"Sugar level":15, "Blood pressure":32, "Heartbeat rate":71, "weight":65, "fat percentage":10.

2. Get values from the user and compare inputs with healthy patient data. If the patient data is not matching with the healthy
patient’s data, provide a warning.

3. Provide difference in readings to the patient.

"""

healthy_data = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}

user_data = {}
for key in healthy_data:
    user_data[key] = float(input(f"Enter {key}: "))
print("\nHealth Report:")
for key in healthy_data:
    if user_data[key] != healthy_data[key]:
        difference = user_data[key] - healthy_data[key]
        print(f"Warning: {key} is not matching! Difference: {difference}")
    else:
        print(f"{key} is normal.")

"""
- Here to find the difference of similar values keys are matched and sytaxed together 
  for comparison and make differences
"""