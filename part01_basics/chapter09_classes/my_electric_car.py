# Storing Multiple Class in a Module
from electric_car_3 import ElectricCar

my_tesla = ElectricCar("tesla", "model S", 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 2016 Tesla Model S
# This car has a 70-kWh battery.
# This car can go approximately 240 miles in a full charge.
