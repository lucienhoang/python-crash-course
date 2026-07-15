lists = []

# add
lists.append('vi em')
lists.append("towm")
lists.append("river")

print(lists)

# add with index
lists.insert(2, 'lau dai')
print(lists)

# delete 
del(lists[0])
print(lists)

# delete but still remember the item
lists.pop(0) # pop()
print(lists)

# removing by value
lists.remove('lau dai')
print(lists)

# add again
lists.append('vi em')
lists.append("towm")
lists.append("lau dai")

# sort
print(" === SORT ===")
lists.sort()
print(lists)

print("Here is the sorted list:")
print(sorted(lists, reverse= True))

lists.sort(reverse= True)
print(lists)

# reverse
print("Here is the reverse list:")
lists.reverse()
print(lists)

# length
print("Total length of the list: " + str(len(lists)))
