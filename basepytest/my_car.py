from car import Car

my_new_car = Car('audi', 'a5', 2017)
print(my_new_car.get_descriptive_name())


# my_tesla = ElectricCar('tesla', 'moesl s', 2017)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.set_battery_size(85)
# my_tesla.battery.get_range()
my_tesla = ElectricCar('tesla', 'moesl s', 2017)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()