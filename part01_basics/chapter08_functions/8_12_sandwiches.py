def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


make_sandwich("pepper", "meat", "salad")
make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "tomato")

# Making a sandwich with the following items:
# - pepper
# - meat
# - salad
# Making a sandwich with the following items:
# - ham
# - cheese
# Making a sandwich with the following items:
# - turkey
# - lettuce
# - tomato
