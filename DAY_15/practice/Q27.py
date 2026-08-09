# Q27. Create Vehicle -> Car -> ElectricCar using multilevel inheritance.

class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


class ElectricCar(Car):

    def charge(self):
        print("Electric car is charging")


car1 = ElectricCar()

car1.start()
car1.drive()
car1.charge()