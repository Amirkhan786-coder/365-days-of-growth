# largest without max()

numbers = (10, 50, 20, 80, 30)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)