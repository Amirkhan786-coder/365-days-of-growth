# count positive and negative

numbers = (-10, 20, -30, 40, -50, 60)

positive = 0
negative = 0

for number in numbers:
    if number >= 0:
        positive += 1
    else:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)