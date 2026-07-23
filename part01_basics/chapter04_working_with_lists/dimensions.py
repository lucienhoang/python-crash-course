#  Tuples - list of items that cannot change
dimensions = (20, 50)

# print(dimensions[0])
# print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Original dimensions:
# 20
# 50

# redefine the entire tuples
dimensions = (200, 500)
for dimension in dimensions:
    print(dimension)
# 200
# 500
