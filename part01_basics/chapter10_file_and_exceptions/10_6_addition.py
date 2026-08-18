number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

try:
    result = int(number_1) + int(number_2)
except ValueError:
    msg = "You have to enter a number!"
    print(msg)
else:
    print(f"\n{number_1} + {number_2} = {result}")

# Enter the first number: 2
# Enter the second number: a
# You have to enter a number!
