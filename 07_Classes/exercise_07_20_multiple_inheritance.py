class Engine:
    """Class Engine"""
    def start_engine(self):
        """Start engine"""
        print('Engine started!')


class Wheels:
    """Class Wheels"""
    def rotate_wheels(self):
        """Rotate wheels"""
        print('Wheels are rotating!')


class Car(Engine, Wheels):
    """Class Car that inherits from Engine and Wheels"""
    pass


car = Car()
car.start_engine()
car.rotate_wheels()
