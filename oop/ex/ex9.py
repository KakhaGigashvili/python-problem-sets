class Car: 
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""

        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 100

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive naem.""" 
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statment showing the car's mileage"""
        print(f"This car has {self.__odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.__odometer_reading += miles
    
    def fill_gas_tank(self):
        print("Filling gas tank...")

class Battery():
    """A simple attemt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} -kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270

        massage = f"This car can go {self.range}"
        print(massage)
        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vechicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parrent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} -kwh battery")

    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar("tesla", "model s", 2024)
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

