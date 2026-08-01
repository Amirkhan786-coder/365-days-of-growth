# count even and odd

numbers = (10, 15, 20, 25, 30, 35)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)