#!/usr/bin/python3
from vehicles import *

if __name__ == '__main__':
    my_car = Car("978g3jxo5u13l4", "Toyota", "Camry", 2013, "red", 4, 5)
    airliner = Plane("Boeing", "737", 2019, "light blue", 34.32, True, {1: "Turbine", 2: "Turbine"}, 148)
    some_boat = Boat("Yamaha", "242X", 2022, "blue", "speedboat", "gas", 8)

    my_car.print_details()
    print()
    airliner.print_details()
    print()
    some_boat.print_details()
    print()
    print("Number of vehicles: {}".format(len(Vehicle.all_vehicles)))
    print()
    my_car.__del__()
    print()
    print("Number of vehicles: {}".format(len(Vehicle.all_vehicles)))
    print("\nProgram ended.")
