def city_country(city, country):
    prompt = f"{city.title()}, {country.title()}!"
    return prompt


city1 = city_country("buon ma thuot", "viet nam")
print(city1)
# Buon Ma Thuot, Viet Nam!

city2 = city_country("seoul", "south korea")
print(city2)
# Seoul, South Korea!
