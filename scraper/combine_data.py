from extract_gdp import extract_gdp
from extract_population_region import extract_population_and_region
import json


def combine_data():
    population_data = extract_population_and_region()
    gdp_data = extract_gdp()

    combined = {}

    for country, pop_info in population_data.items():
        combined[country] = {
            **pop_info,
            **gdp_data.get(country, {
                "gdp": None,
                "gdp_full_value": None,
                "gdp_growth": None,
                "gdp_per_capital": None
            })
        }
    try:
        with open("../countries_data.json", "w") as file:
            json.dump(combined, file, indent=4)
    except Exception as e:
        print(f"An error occured: {e}")

