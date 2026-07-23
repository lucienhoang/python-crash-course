my_foods = ["banh xeo", "banh hoi", "banh beo", "banh canh"]

# copyying a list must use Slice ":"
friend_foods = my_foods[:]

my_foods.append("coconut")
friend_foods.append("ice cream")

print("My favorite food are:")
print(my_foods)
# My favorite food are:
# ['banh xeo', 'banh hoi', 'banh beo', 'banh canh', 'coconut']

print("\nMy friend's favorite food are:")
print(friend_foods)
# My friend's favorite food are:
# ['banh xeo', 'banh hoi', 'banh beo', 'banh canh', 'ice cream']

for food in friend_foods:
    print(food)
# banh xeo
# banh hoi
# banh beo
# banh canh
# ice cream
