# list example
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized']

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())
# trek
# Trek

# Index positions
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])  # === print(bicycles[3])
# cannondale
# specialized
# specialized

# Using  Individual Values from a List
message = "My first bicyles was a " + bicycles[0].title() + "."
print(message)
# My first bicyles was a Trek.
