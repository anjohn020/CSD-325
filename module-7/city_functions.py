# city_functions.py

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population is not None:
        result += f" - population {population}"
    if language is not None:
        result += f", {language.title()}"
    return result


def run_examples():
    print(city_country("santiago", "chile"))
    print(city_country("santiago", "chile", 5000000))
    print(city_country("santiago", "chile", 5000000, "spanish"))


if __name__ == "__main__":
    run_examples()