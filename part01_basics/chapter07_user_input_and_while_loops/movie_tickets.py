prompt = "\nTell me your age, and i will tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to end the program. "

while True:
    age = input(prompt)

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("The ticket is free.")
    elif age <= 12:
        print("The ticket is 10$.")
    else:
        print("The ticket is 15$.")

# Tell me your age, and i will tell you the cost of your movie ticket.
# Enter 'quit' to end the program. 2
# The ticket is free.

# Tell me your age, and i will tell you the cost of your movie ticket.
# Enter 'quit' to end the program. 5
# The ticket is 10$.

# Tell me your age, and i will tell you the cost of your movie ticket.
# Enter 'quit' to end the program. 15
# The ticket is 15$.

# Tell me your age, and i will tell you the cost of your movie ticket.
# Enter 'quit' to end the program. quit
