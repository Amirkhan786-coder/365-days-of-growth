# ARMSTRONG

print("Armstrong Numbers from 1 to 1000\n")

for num in range(1, 1001):
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num)