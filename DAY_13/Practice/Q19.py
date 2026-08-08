# Q19. Convert JSON data into Python dictionary.

import json

json_data = '{"name": "Amir", "age": 20}'

student = json.loads(json_data)

print("Name:", student["name"])
print("Age:", student["age"])