def formatted_city_country(city,country, population=''):
    return f"{city.title()}, {country.title() if population == '' else f",{population}" }"