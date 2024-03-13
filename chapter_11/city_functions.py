def get_city(city, country, population=None):
    """Accept and return a single string with city and country"""
    city_name = city
    country_name = country
    pop = population
    city_info = f"{city_name.title()}, {country_name.title()} - population {pop}"
    return city_info