sandwich_orders = ["Ham & Cheese", "Egg", "Tuna", "Panini"]
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made you a {current_order} sandwiche")
    finished_sandwiches.append(current_order)

print("\n--- Sandwiches made ---")
for sandwich in finished_sandwiches:
    print(sandwich)

# I made you a Ham & Cheese sandwiche
# I made you a Egg sandwiche
# I made you a Tuna sandwiche
# I made you a Panini sandwiche

# --- Sandwiches made ---
# Ham & Cheese
# Egg
# Tuna
# Panini
