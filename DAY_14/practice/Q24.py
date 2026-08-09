# Multiple Cars

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


car1 = Car("Toyota", "Fortuner", 4000000)
car2 = Car("BMW", "X5", 9500000)
car3 = Car("Audi", "Q7", 8500000)

car1.display()
print()

car2.display()
print()

car3.display()