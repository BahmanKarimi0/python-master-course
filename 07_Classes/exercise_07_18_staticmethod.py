class Car:
    """Class Car"""
    @staticmethod
    def is_motor_vehicle():
        """Show that the car is moving"""
        return True


car = Car()
print(car.is_motor_vehicle())
print(Car.is_motor_vehicle())