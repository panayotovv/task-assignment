import json

def most_populated_countries(region=None):
    with open("countries_data.json", "r") as file:
        data = json.load(file)

    countries = {}

    for country, info in data.items():
        if region and info.get("region") != region:
            continue

        population = int(info["population"].replace(",", ""))
        countries[country] = population

    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)

    top_5 = sorted_countries[:5]

    result = {}

    for country, pop in top_5:
        result[country] = f"{pop:,}"

    return {
        "region": region,
        "top_countries": result
    }