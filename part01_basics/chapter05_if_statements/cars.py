cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Audi
# BMW
# Subaru
# Toyota

car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")
# Is car == 'subaru'? I predict True.
# True

print("\nIs car == 'huyndai'? I predict False.")
print(car == "huyndai")
# Is car == 'huyndai'? I predict False.
# False

car = "yamaha"
print("\nIs car == 'yamaha'? I predict True.")
print(car == "yamaha")
# Is car == 'yamaha'? I predict True.
# True
