def make_car(manufacturer, model, **details):
    """Store car's information in a dictionary"""
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for key, value in details.items():
        car[key] = value

    return car


car = make_car("subaru", "black", color="blue", tow_package="True")

print(car)

# {'manufacturer': 'subaru', 'model': 'black', 'color': 'blue', 'tow_package': 'True'}
