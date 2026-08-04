# Question: Modify a global variable using the global keyword.

count = 0

def increase():
    global count
    count += 1

increase()

print("Count:", count)