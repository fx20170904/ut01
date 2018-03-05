"""餐馆的类"""
class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.flavors = []
    def describe_restaurant(self):
        print("The name of the restaurant is " + str(self.restaurant_name) + ".It's cuisine type is " +
              str(self.cuisine_type))

    def open_restaurant(self):
        print('OPEN')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, number):
        self.number_served += number

    def set_flavors(self, stand):
        self.flavors = stand

    def show_flavors(self):
        print(self.flavors)
