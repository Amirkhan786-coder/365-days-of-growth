# tuple input form user 

numbers = tuple(
    map(
        int,
        input("Enter numbers separated by space: ").split()
    )
)

print("Tuple:", numbers)