# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green pepper", "extra cheese")


# Making a 16-inch pizza with the following toppings:
# - pepperoni

# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green pepper
# - extra cheese
