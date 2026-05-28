import json

def list_all_countries_by_region():
    with open("countries_data.json", "r") as file:
        data = json.load(file)

    region_input = input("Please enter a region: ")

    countries = []

    for country, info in data.items():
        if info.get("region") == region_input:
            countries.append(country)

    return {
        "region": region_input,
        "countries": countries
    }