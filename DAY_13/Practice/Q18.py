# Q18. Convert Python dictionary into JSON.

import json

student = {
    "name": "Amir",
    "age": 20,
    "course": "B.Tech CSE"
}

json_data = json.dumps(student)

print(json_data)