responses = {}
name_prompt = "\nWhat is your name? "
question_prompt = "If you could visit one place in the world, where would you go? "
yes_no_prompt = "Would you like to let another respond? (yes/no) "

while True:
    name = input(name_prompt)
    destination = input(question_prompt)

    responses[name] = destination

    respond = input(yes_no_prompt)
    if respond.lower() == "no":
        break

print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go {response.title()}")


# What is your name? luci
# If you could visit one place in the world, where would you go? da nang
# Would you like to let another respond? (yes/no) yes

# What is your name? laurence
# If you could visit one place in the world, where would you go? nha trang
# Would you like to let another respond? (yes/no) no

# --- Poll Result ---
# Luci would like to go Da Nang
# Laurence would like to go Nha Trang
