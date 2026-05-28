from analysis.highest_gdp_countries import highest_gdp_countries
from analysis.most_populated_countries import most_populated_countries


def most_populated_or_highest_gdp():
    region = input("Please enter a region: ")
    attr = input("Please enter an attribute: ")

    if attr.lower() == "gdp":
        return highest_gdp_countries(region)
    elif attr.lower() == "population":
        return most_populated_countries(region)
    else:
        return {"error": "Invalid attribute"}

print(most_populated_or_highest_gdp())
