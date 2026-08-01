# Find students with highest marks

students = (
    ("Amir", 85),
    ("Rahul", 90),
    ("Aman", 78)
)

topper = students[0]

for student in students:
    if student[1] > topper[1]:
        topper = student

print("Topper:", topper[0])
print("Marks:", topper[1])