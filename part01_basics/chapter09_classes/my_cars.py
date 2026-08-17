# Importing Multiple Classes from a Module
from electric_car_3 import Car, ElectricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "roaster", 2016)
print(my_tesla.get_descriptive_name())

# 2016 Volkswagen Beetle
# 2016 Tesla Roaster
