lists = []

# add
lists.append("vi em")
lists.append("towm")
lists.append("river")

print(lists)
# ['vi em', 'towm', 'river']

# add with index
lists.insert(2, "lau dai")
print(lists)
# ['vi em', 'towm', 'lau dai', 'river']

# delete
del lists[0]
print(lists)
# ['towm', 'lau dai', 'river']

# delete but still remember the item
lists.pop(0)  # pop()
print(lists)
# ['lau dai', 'river']

# removing by value
lists.remove("lau dai")
print(lists)
# ['river']

# add again
lists.append("vi em")
lists.append("towm")
lists.append("lau dai")

# sort
print(" === SORT ===")
lists.sort()
print(lists)
# ['lau dai', 'river', 'towm', 'vi em']

print("Here is the sorted list:")
print(sorted(lists, reverse=True))
# ['vi em', 'towm', 'river', 'lau dai']

lists.sort(reverse=True)
print(lists)
# ['vi em', 'towm', 'river', 'lau dai']

# reverse
print("Here is the reverse list:")
lists.reverse()
print(lists)
# ['lau dai', 'river', 'towm', 'vi em']

# length
print("Total length of the list: " + str(len(lists)))
# Total length of the list: 4
