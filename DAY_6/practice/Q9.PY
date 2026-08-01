# extended tuple unpacking

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)