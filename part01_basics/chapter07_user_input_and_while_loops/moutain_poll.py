reponses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    reponse = input("Which moutain would you like to climb someday? ")

    # Store the reponse in the dictionary:
    reponses[name] = reponse

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# Polling is complete. Show the result.
print("\n--- Poll Results ---")
for name, reponse in reponses.items():
    print(f"{name.title()} would like to climb {reponse.title()}")

# What is your name? khoa
# Which moutain would you like to climb someday? phu si
# Would you like to let another person respond? (yes/no) yes

# What is your name? dung
# Which moutain would you like to climb someday? sa pa
# Would you like to let another person respond? (yes/no) no

# --- Poll Results ---
# Khoa would like to climb Phu Si
# Dung would like to climb Sa Pa
