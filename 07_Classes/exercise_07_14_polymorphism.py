class Car:
    def display_info(self):
        print('This is car!')


class Bike:
    def display_info(self):
        print('This is bike!')


car = Car()
bike = Bike()


def display_obj(obj):
    for i in obj:
        i.display_info()


display_obj([car, bike])
