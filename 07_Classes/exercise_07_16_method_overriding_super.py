class Vehicle:
    """Class Vehicle"""
    def display_info(self):
        """Shows information about the vehicle"""
        print('This is vehicle')


class Car(Vehicle):
    """Class Car"""
    def display_info(self):
        """Shows information about the car"""
        super().display_info()
        print('This is car')


car = Car()

car.display_info()
