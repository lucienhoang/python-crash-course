requested_topping = "mushrooms"

if requested_topping != "anchoives":
    print("Hold the Anchoives!")

# requested_toppings = ["mushrooms", "extra cheese", "pepper"]
requested_toppings = []


# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms.")
# if "pepper" in requested_toppings:
#     print("Adding pepper.")
# if "extra cheese" in requested_toppings:
#     print("Adding extra cheese.")

if requested_toppings:  # return true if requested_toppings is not null
    for requested_topping in requested_toppings:
        if requested_topping == "mushrooms":
            print("Sorry, We are out of mushrooms right now!")
        else:
            print("Adding " + requested_topping.title() + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# test
