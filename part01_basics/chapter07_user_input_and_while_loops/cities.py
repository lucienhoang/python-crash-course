prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Please enter the name of a city you have visited.
# (Enter 'quit' when you are finished.)ha noi
# I'd love to go to Ha Noi!

# Please enter the name of a city you have visited.
# (Enter 'quit' when you are finished.)ho chi minh
# I'd love to go to Ho Chi Minh!

# Please enter the name of a city you have visited.
# (Enter 'quit' when you are finished.)quit
