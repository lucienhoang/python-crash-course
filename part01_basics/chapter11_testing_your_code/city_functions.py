def city_country(city_name, country_name, population=""):
    """Return a neatly formatted city, country name."""
    if population:
        msg = f"{city_name.title()}, {country_name.title()} - population {population}."
    else:
        msg = f"{city_name.title()}, {country_name.title()}."
    return msg
