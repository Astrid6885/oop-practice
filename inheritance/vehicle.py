"""Inheritance - Problem 1: Vehicle, Car and Bicycle."""


class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):  # overrides Vehicle.drive
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):  # overrides Vehicle.drive
        return "Riding a bicycle"


if __name__ == "__main__":
    # Polymorphism: same method name, different behaviour
    for vehicle in [Vehicle(), Car(), Bicycle()]:
        print(vehicle.drive())
