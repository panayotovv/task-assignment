import json
def total_and_average_population_gdp_per_region():

    with open("countries_data.json", "r") as file:
        data = json.load(file)

    region_input = input("Please enter a region: ")

    total_population = 0
    total_gdp = 0
    count = 0

    for country, info in data.items():
        if info.get("region") != region_input:
            continue

        count += 1

        pop_raw = info.get("population", "0").replace(",", "")
        if pop_raw.isdigit():
            population = int(pop_raw)
        else:
            population = 0

        gdp_raw = info.get("gdp_full_value")
        if gdp_raw:
            try:
                gdp = int(gdp_raw.replace("$", "").replace(",", "").strip())
            except:
                gdp = 0
        else:
            gdp = 0

        total_population += population
        total_gdp += gdp

    if count == 0:
        return {
            "region": region_input,
            "error": "No countries found"
        }

    average_gdp = total_gdp / count
    average_population = total_population / count

    return {
        "region": region_input,
        "total_population": f"{total_population:,}",
        "total_gdp": f"{total_gdp:,}",
        "average_gdp": round(average_gdp, 2),
        "average_population": round(average_population, 2)
    }