class Restaurant:
    """A simple class to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describle_restaurant(self):
        print(f"\n{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def show_number_served(self):
        print(f"\n{self.restaurant_name} has served {self.number_served} customers.")