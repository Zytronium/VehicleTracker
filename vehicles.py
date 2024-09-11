#!/usr/bin/python3
"""
module for a vehicle tracker
"""
from logging import exception


class Vehicle:
    all_vehicles = []

    def __init__(self, make, model, year, color="white"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Vehicle.all_vehicles.append(self)

    def __del__(self):
        try:
            del_msg = "A {} {} {} {} was totaled.".format(self.color, self.year, self.make, self.model)
            Vehicle.all_vehicles.remove(self)
            del self
            print(del_msg)
        except ValueError:
            pass

    def print_details(self, type=None):
        print("Vehicle Details:")
        print("Type: {}".format(type))
        print("Make: {}".format(self.make))
        print("Model: {}".format(self.model))
        print("Year: {}".format(self.year))
        print("Color: {}".format(self.color))

class Car(Vehicle):
    all_cars = []
    def __init__(self, vin, make, model, year, color="white", doors=4, seats=4):
        super().__init__(make, model, year, color)
        self.__vin = vin
        self.number_of_doors = doors
        self.number_of_seats = seats
        if type(vin) is not str:
            raise TypeError("VIN must be a string")
        if not vin.isalnum():
            raise ValueError("VIN must be alphanumeric")
        # Todo: check all other cars and motorcycles to see if this vin is taken
        Car.all_cars.append(self)

    def __del__(self):
        super().__del__()
        try:
            Car.all_cars.remove(self)
            del self
        except ValueError:
            pass

    def print_details(self, type="Car"):
        super().print_details(type)
        print("VIN #: {}".format(self.__vin))
        print("Number of doors: {}".format(self.number_of_doors))
        print("Number of seats: {}".format(self.number_of_seats))

    @property
    def vin(self):
        """
        retrieves the vehicle's VIN
        :return: the vehicle's VIN
        """
        return self.__vin

    @vin.setter
    def vin(self, new_vin):
        """
        changes the vehicle's VIN. But why would you need to do that?
        :param new_vin: the new vehicle's VIN. Must be an alphanumeric string.
        """
        if type(new_vin) is not str:
            raise TypeError("VIN must be a string")
        if not new_vin.isalnum():
            raise ValueError("VIN must be alphanumeric")
        # Todo: check all other cars and motorcycles to see if this vin is taken
        self.__vin = new_vin

class Motorcycle(Vehicle):
    all_motorcycles = []
    def __init__(self, vin, make, model, year, color="white", has_sidecar=False):
        super().__init__(make, model, year, color)
        self.__vin = vin
        self.has_sidecar = has_sidecar
        if type(vin) is not str:
            raise TypeError("VIN must be a string")
        if not vin.isalnum():
            raise ValueError("VIN must be alphanumeric")
        # Todo: check all other cars and motorcycles to see if this vin is taken
        Motorcycle.all_motorcycles.append(self)

    def __del__(self):
        super().__del__()
        Motorcycle.all_motorcycles.remove(self)

    def print_details(self, type="Motorcycle"):
        super().print_details(type)
        print("VIN #: {}".format(self.__vin))
        print("Has sidecar: {}".format(self.has_sidecar))

    @property
    def vin(self):
        """
        retrieves the vehicle's VIN
        :return: the vehicle's VIN
        """
        return self.__vin

    @vin.setter
    def vin(self, new_vin):
        """
        changes the vehicle's VIN. But why would you need to do that?
        :param new_vin: the new vehicle's VIN. Must be an alphanumeric string.
        """
        if type(new_vin) is not str:
            raise TypeError("VIN must be a string")
        if not new_vin.isalnum():
            raise ValueError("VIN must be alphanumeric")
        # Todo: check all other cars and motorcycles to see if this vin is taken
        self.__vin = new_vin

class Plane(Vehicle):  # wingspan is in meters
    all_planes = []
    def __init__(self, make, model, year, color="white", wingspan=10.0, retractable_gear=True, engines: dict = {1: "piston"}, seats=2):
        super().__init__(make, model, year, color)
        self.wingspan = wingspan
        self.retractable_gear = retractable_gear
        self.engines = engines
        self.seats = seats
        Plane.all_planes.append(self)

    def __del__(self):
        super().__del__()
        Plane.all_planes.remove(self)

    def print_details(self, type="Plane"):
        super().print_details(type)
        print("Wingspan: {:.2f} Meters".format(self.wingspan))
        print("Gear is Retractable: {}".format(self.retractable_gear))
        print("Engines: {}".format(self.engines))
        print("Number of Seats: {}".format(self.seats))

class Boat(Vehicle):  # wingspan is in meters
    all_boats = []
    def __init__(self, make, model, year, color="white", type="speedboat", engine_type="gas", seats=6):
        super().__init__(make, model, year, color)
        self.type = type
        self.engine_type = engine_type
        self.seats = seats
        Boat.all_boats.append(self)

    def __del__(self):
        super().__del__()
        Boat.all_boats.remove(self)

    def print_details(self, type="Boat"):
        super().print_details(type)
        print("Type of Boat: {}".format(self.type))
        print("Engine Type: {}".format(self.engine_type))
        print("Number of Seats: {}".format(self.seats))
