# ============================================================
# Q25. TEMPERATURE CONVERTER
# Convert Celsius to Fahrenheit and Fahrenheit to Celsius.
# ============================================================

try:
    choice = input(
        "Enter C for Celsius to Fahrenheit "
        "or F for Fahrenheit to Celsius: "
    ).upper()

    temperature = float(input("Enter temperature: "))

    if choice == "C":
        result = (temperature * 9 / 5) + 32
        print("Fahrenheit:", result)

    elif choice == "F":
        result = (temperature - 32) * 5 / 9
        print("Celsius:", result)

    else:
        raise ValueError("Invalid conversion choice.")

except ValueError as e:
    print("Error:", e)