sandwich_orders = [
    "Ham & Cheese",
    "pastrami",
    "Egg",
    "pastrami",
    "Tuna",
    "Panini",
    "pastrami",
]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made you a {current_order} sandwich")
    finished_sandwiches.append(current_order)

print("\n--- Sandwiches made ---")
for sandwich in finished_sandwiches:
    print(sandwich)

# The deli has run out of pastrami.
# I made you a Ham & Cheese sandwich
# I made you a Egg sandwich
# I made you a Tuna sandwich
# I made you a Panini sandwich

# --- Sandwiches made ---
# Ham & Cheese
# Egg
# Tuna
# Panini
