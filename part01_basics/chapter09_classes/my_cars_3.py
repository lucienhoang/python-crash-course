# Importing a Module into a Module
from car_5 import Car
from electric_car_4 import ElectricCar


my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roaster", 2016)
print(my_tesla.get_descriptive_name())

# 2016 Volkswagen Beetle
# 2016 Tesla Roaster
