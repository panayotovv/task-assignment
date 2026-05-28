import json

def highest_gdp_countries(region=None):
    with open("../countries_data.json", "r") as file:
        data = json.load(file)

    countries = {}

    for country, info in data.items():
        if region and info.get("region") != region:
            continue

        gdp_raw = info.get("gdp_full_value")

        if not gdp_raw:
            continue

        try:
            gdp = int(gdp_raw.replace("$", "").replace(",", "").strip())
        except:
            gdp = 0

        countries[country] = gdp

    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)

    top_5 = sorted_countries[:5]

    result = {}

    for country, gdp in top_5:
        result[country] = f"{gdp:,}"

    return {
        "region": region,
        "top_countries": result
    }