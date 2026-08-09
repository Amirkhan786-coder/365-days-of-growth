# Q3. Create a Vehicle class and inherit it into a Car class.

class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


car1 = Car()
car1.start()
car1.drive()