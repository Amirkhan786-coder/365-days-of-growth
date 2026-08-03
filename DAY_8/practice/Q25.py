# Question:
# Create a dictionary from two lists using zip().

keys = ["Name", "Age", "City"]

values = ["Amir", 19, "Meerut"]

student = dict(zip(keys, values))

print(student)