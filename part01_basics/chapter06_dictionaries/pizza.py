### A list in a Dictionary

# Store  information about a pizza being ordered.
pizza = {"crust": "thick", "topping": ["mushrooms", "extra cheese"]}
# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following topping:")
for topping in pizza["topping"]:
    print(f"\t{topping}")

# You ordered a thick-crust pizza with the following topping:
#         mushrooms
#         extra cheese
