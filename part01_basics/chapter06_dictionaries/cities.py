cities = {
    "Ho Chi Minh": {
        "country": "Viet Nam",
        "population": "8 milions",
        "fact": "super hot",
    },
    "Seoul": {
        "country": "Korean",
        "population": "10 milions",
        "fact": "high living standard",
    },
    "New York": {
        "country": "USA",
        "population": "15 milions",
        "fact": "a lot of pretty girls",
    },
}

for index, (cities_name, cities_information) in enumerate(cities.items(), start=1):
    print(f"{index}. City: {cities_name}")
    country = cities_information["country"]
    population = cities_information["population"]
    fact = cities_information["fact"]
    print(f"    Country: {country.title()}")
    print(f"    Population: {population.title()}")
    print(f"    Fact: {fact.title()}")

# 1. City: Ho Chi Minh
#     Country: Viet Nam
#     Population: 8 Milions
#     Fact: Super Hot
# 2. City: Seoul
#     Country: Korean
#     Population: 10 Milions
#     Fact: High Living Standard
# 3. City: New York
#     Country: Usa
#     Population: 15 Milions
#     Fact: A Lot Of Pretty Girls
