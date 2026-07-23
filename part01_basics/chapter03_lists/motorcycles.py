motorcycles = ["honda", "suzuki", "yamaha"]
print(motorcycles)
# ['honda', 'suzuki', 'yamaha']

# Modifying elements in a List
motorcycles[0] = "ducati"
print(motorcycles)
# ['ducati', 'suzuki', 'yamaha']

# Adding elements to a List
motorcycles.append("Pioneer 1")
print(motorcycles)
# ['ducati', 'suzuki', 'yamaha', 'Pioneer 1']

# Removing an Item using the Del Statement
del motorcycles[3]
print(motorcycles)
# ['ducati', 'suzuki', 'yamaha']

# Removing an Item using the Pop() method
popped_motorcycles = motorcycles.pop()
print(motorcycles)
# ['ducati', 'suzuki']
print(popped_motorcycles)  # yamaha
print("The last motorcycles that i owned was a " + popped_motorcycles.title() + ".")
# The last motorcycles that i owned was a Yamaha.

# first_owned = motorcycles.pop(0)
# print("The first motorcycles that i owned was a " + first_owned.title() + ".")

# Removing an Item by value
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
# ['suzuki']
print("\nA " + too_expensive.title() + " is too expensive for me.")
# A Ducati is too expensive for me.
