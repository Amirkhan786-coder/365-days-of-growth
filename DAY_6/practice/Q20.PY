# smallest without min()

numbers = (10, 50, 20, 80, 30)

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)