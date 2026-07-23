age = 66

# if age < 4:
#     print("Your cost is $0.")
# elif age < 18:
#     print("Your cost is $5.")
# else:
#     print("Your cost is $10.")

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:  # else:
    price = 6

print("Your cost is $" + str(price) + ".")
# Your cost is $6.
