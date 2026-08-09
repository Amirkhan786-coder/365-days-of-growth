# Q26. Create Vehicle -> Bike using inheritance.

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "vehicle started")


class Bike(Vehicle):

    def ride(self):
        print(self.brand, "bike is riding")


bike1 = Bike("Honda")

bike1.start()
bike1.ride()