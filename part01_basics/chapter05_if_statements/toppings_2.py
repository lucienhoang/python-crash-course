available_toppings = [
    "mushrooms",
    "olives",
    "green pepper",
    "pineaplle",
    "extra cheese",
]

requested_toppings = ["mushrooms", "extra cheese", " green pepper"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping.title() + ".")
    else:
        print("Sorry, we don't have " + requested_topping.title())
print("\nFinished making your pizza!")
