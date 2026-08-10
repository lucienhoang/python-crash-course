import printing_function


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

printing_function.print_models(unprinted_designs[:], completed_models)
# The Slice [:] notation makes a copy of the list to send to the function.
show_completed_models(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case

# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case
