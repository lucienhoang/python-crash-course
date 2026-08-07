def describe_pet(animal_type, pet_name):  # Positional arguments
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("dog", "bi xanh")
describe_pet("cat", "bun")


# I have a dog.
# My dog's name is Bi Xanh

# I have a cat.
# My cat's name is Bun
