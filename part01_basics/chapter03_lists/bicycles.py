# list example
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

# Index positions
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])  # === print(bicycles[3])

# Using  Individual Values from a List
message = "My first bicyles was a " + bicycles[0].title() + "."
print(message)
