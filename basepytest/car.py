"""一个可以表示汽车的类"""

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """将里程数设置为指定值"""
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        """将里程表读数增加制定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('fill')


class Battery():

    def __init__(self, battery_size=70):

        self.battery_size = battery_size

    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 85:
            range = 280
        elif self.battery_size == 70:
            range = 250
        else:
            range = 0
        print("This car can go approximately " + str(range) + ' miles on a full charge.')

    def set_battery_size(self, size):
        self.battery_size = size

    def upgrade_battery(self):
        self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('no tank')