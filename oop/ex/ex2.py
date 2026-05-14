class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        result = f"{self.restaurant_name} {self.cuisine_type}"
        print(result.title())

    def open_restaurant(self):

        massage = f"{self.restaurant_name} is open"
        print(massage)

restaurant_ita = Restaurant("kanto", "Italian Kitchen")
restaurant_asian = Restaurant("mushu", "asian kitchen")
restaurant_geo = Restaurant("sakhli", "Georgian Kitchen")


restaurant_ita.describe_restaurant()
restaurant_asian.describe_restaurant()
restaurant_geo.describe_restaurant()

