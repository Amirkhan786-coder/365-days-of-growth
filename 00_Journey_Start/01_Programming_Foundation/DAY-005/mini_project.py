# ==========================================
# DAY 005 — MINI PROJECT
# STUDENT BILL & SAVINGS CALCULATOR
# ==========================================

print("=" * 55)
print("       STUDENT SHOPPING & SAVINGS CALCULATOR")
print("=" * 55)

# ------------------------------------------
# 1. STUDENT DETAILS
# ------------------------------------------

name = input("Enter your name: ")

# ------------------------------------------
# 2. PRODUCT DETAILS
# ------------------------------------------

print("\nEnter Product Details")

product1 = input("Product 1 name: ")
price1 = float(input("Product 1 price: "))
quantity1 = int(input("Product 1 quantity: "))

product2 = input("Product 2 name: ")
price2 = float(input("Product 2 price: "))
quantity2 = int(input("Product 2 quantity: "))

product3 = input("Product 3 name: ")
price3 = float(input("Product 3 price: "))
quantity3 = int(input("Product 3 quantity: "))


# ------------------------------------------
# 3. CALCULATE PRODUCT TOTALS
# ------------------------------------------

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

subtotal = total1 + total2 + total3


# ------------------------------------------
# 4. DISCOUNT CALCULATION
# ------------------------------------------

discount_percentage = 10

discount_amount = subtotal * discount_percentage / 100

final_amount = subtotal - discount_amount


# ------------------------------------------
# 5. PAYMENT
# ------------------------------------------

print("\nPayment Details")

payment = float(input("Enter amount paid: "))

remaining = final_amount - payment


# ------------------------------------------
# 6. DISPLAY BILL
# ------------------------------------------

print("\n")
print("=" * 55)
print("                 FINAL BILL")
print("=" * 55)

print("Student Name:", name)

print("-" * 55)

print(
    product1,
    "x",
    quantity1,
    "=",
    total1
)

print(
    product2,
    "x",
    quantity2,
    "=",
    total2
)

print(
    product3,
    "x",
    quantity3,
    "=",
    total3
)

print("-" * 55)

print("Subtotal           :", subtotal)
print("Discount (10%)     :", discount_amount)
print("Final Amount       :", final_amount)
print("Amount Paid        :", payment)


# ------------------------------------------
# 7. PAYMENT STATUS
# ------------------------------------------

if payment >= final_amount:
    change = payment - final_amount

    print("Change             :", change)
    print("Payment Status     : PAID")

else:
    due = final_amount - payment

    print("Amount Due         :", due)
    print("Payment Status     : PENDING")


# ------------------------------------------
# 8. SAVING CALCULATION
# ------------------------------------------

print("\n")
print("=" * 55)
print("                 SAVING DETAILS")
print("=" * 55)

print("You saved          :", discount_amount)
print("Savings Percentage :", discount_percentage, "%")


# ------------------------------------------
# 9. FINAL SUMMARY
# ------------------------------------------

print("\n")
print("=" * 55)
print("                 SUMMARY")
print("=" * 55)

print("Student :", name)
print("Items   :", quantity1 + quantity2 + quantity3)
print("Subtotal:", subtotal)
print("Saved   :", discount_amount)
print("Payable :", final_amount)

print("=" * 55)
print("       THANK YOU FOR USING THE PROGRAM 🚀")
print("=" * 55)