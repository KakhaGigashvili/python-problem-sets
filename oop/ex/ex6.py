class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        result = f"{self.restaurant_name} {self.cuisine_type}"
        print (result.title())

    def open_restaurant(self):

        massage = f"{self.restaurant_name} is open"

        print(massage)

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors

    def show_flavors(self):
        
        for flavor in self.flavors:
            print(f"{flavor}")

my_icecream = IceCreamStand(
"Sweet Ice",
"Ice Cream",
["Vanilla", "Chocolate", "Strawberry"]
)

my_icecream.describe_restaurant()
my_icecream.show_flavors()
