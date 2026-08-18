while True:
    number_1 = input("Enter the first number (Enter 'q' to quit): ")
    if number_1 == "q":
        break

    number_2 = input("Enter the second number (Enter 'q' to quit): ")
    if number_2 == "q":
        break

    try:
        result = int(number_1) + int(number_2)
    except ValueError:
        msg = "You have to enter a number!"
        print(msg)
    else:
        print(f"\n{number_1} + {number_2} = {result}\n")


# Enter the first number (Enter 'q' to quit): 2
# Enter the second number (Enter 'q' to quit): 5

# 2 + 5 = 7

# Enter the first number (Enter 'q' to quit): 6
# Enter the second number (Enter 'q' to quit): 7

# 6 + 7 = 13

# Enter the first number (Enter 'q' to quit): e
# Enter the second number (Enter 'q' to quit): 4
# You have to enter a number!
# Enter the first number (Enter 'q' to quit): q
