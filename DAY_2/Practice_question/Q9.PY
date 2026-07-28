# Program: Divisible by 5 and 11

num = int(input("Enter Number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11.")
else:
    print("Number is NOT divisible by both 5 and 11.")