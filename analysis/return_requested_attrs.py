import json

def return_requested_attrs():
    with open("countries_data.json", "r") as file:
        data = json.load(file)

    country = input("Please enter a country: ")
    attr = input("Please enter an attribute: ")

    if country not in data:
        return {"error": "Country not found"}

    value = data[country].get(attr.lower(), "Attribute not found")

    return {
        country: {
            attr.upper(): value
        }
    }