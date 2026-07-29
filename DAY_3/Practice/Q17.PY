# PPRIME NUMBER BETWEEN 1 TO 100

print("Prime Numbers from 1 to 100\n")

for num in range(2, 101):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)