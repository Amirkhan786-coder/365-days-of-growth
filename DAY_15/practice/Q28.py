# Q28. Demonstrate polymorphism using different vehicles.

class Car:

    def start(self):
        print("Car starts with a key")


class Bike:

    def start(self):
        print("Bike starts with a button")


class ElectricCar:

    def start(self):
        print("Electric car starts silently")


car = Car()
bike = Bike()
electric_car = ElectricCar()

car.start()
bike.start()
electric_car.start()