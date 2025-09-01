from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for vehicles."""
    @abstractmethod
    def display_info(self):
        """Display information about the vehicle"""


class Car(Vehicle):
    """Car class that inherits from Vehicle"""
    def display_info(self):
        print("Vehicle has a car")


class Bike(Vehicle):
    """Bike class that inherits from Vehicle"""
    def display_info(self):
        print("Vehicle has a bike")


car = Car()
bike = Bike()

for obj in [car, bike]:
    obj.display_info()
