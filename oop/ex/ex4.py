class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):

        result = f"{self.restaurant_name} {self.cuisine_type}"
        print (result.title())

    def open_restaurant(self):

        massage = f"{self.restaurant_name} is open"

        print(massage)
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers

restaurant_ita = Restaurant("Kanto", "Italian Kitchen")
restaurant_asian = Restaurant("mushu", "asian kitchen")

restaurant_asian.describe_restaurant()
restaurant_asian.open_restaurant()
restaurant_asian.set_number_served(8)
print(f"customers served {restaurant_asian.number_served}")

restaurant_asian.increment_number_served(6)
print(f"customers served {restaurant_asian.number_served}")

print("="*50)

restaurant_ita.describe_restaurant()
restaurant_ita.open_restaurant()
restaurant_ita.set_number_served(9)
print(f"customers served {restaurant_ita.number_served}")

restaurant_ita.increment_number_served(5)
print(f"customers served {restaurant_ita.number_served}")