locations = ["Japan", "American", "France", "England", "Swedish"]
print("Five places in the world I want to visit:")
print(locations)
# ['Japan', 'American', 'France', 'England', 'Swedish']

print("Sorted List:")
print(sorted(locations))
# ['American', 'England', 'France', 'Japan', 'Swedish']

print("Original List:")
print(locations)
# ['Japan', 'American', 'France', 'England', 'Swedish']

print("Reverse sorted List:")
print(sorted(locations, reverse=True))
# ['Swedish', 'Japan', 'France', 'England', 'American']

print("Reverse List:")
locations.reverse()
print(locations)
# ['Swedish', 'Japan', 'France', 'England', 'American']

print("Reverse List again:")
locations.reverse()
print(locations)
# ['Japan', 'American', 'France', 'England', 'Swedish']

print("Sort List:")
locations.sort()
print(locations)
# ['American', 'England', 'France', 'Japan', 'Swedish']

print("Sort List Reverse:")
locations.sort(reverse=True)
print(locations)
# ['Swedish', 'Japan', 'France', 'England', 'American']
