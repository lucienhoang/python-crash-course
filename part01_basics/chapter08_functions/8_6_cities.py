def describe_city(name, country="Viet Nam"):
    prompt = f"{name.title()} city is in {country.title()}."
    print(prompt)


describe_city("da nang")
describe_city(name="buon ma thuot")
describe_city(name="New york", country="USA")

# Da Nang city is in Viet Nam.
# Buon Ma Thuot city is in Viet Nam.
# New York city is in Usa.
