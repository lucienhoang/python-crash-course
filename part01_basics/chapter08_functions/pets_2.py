# default value
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name="bi xanh")
describe_pet(pet_name="bun", animal_type="cat")

# I have a dog.
# My dog's name is Bi Xanh

# I have a cat.
# My cat's name is Bun
