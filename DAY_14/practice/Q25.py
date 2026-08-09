#Multiple Mobile Phones

class Mobile:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


mobile1 = Mobile("Samsung", "S25", 80000)
mobile2 = Mobile("Apple", "iPhone 16", 90000)
mobile3 = Mobile("OnePlus", "13", 70000)

mobile1.display()
print()

mobile2.display()
print()

mobile3.display()