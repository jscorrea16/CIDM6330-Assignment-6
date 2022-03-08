# This is just my initial attempt to code my final project.
class Arthropod:
    def __init__(type, insect, arachnid):
        type.insect = insect
        type.arachnid = arachnid


class Geographical:
    def get_location(city_name, county_name):
        return f"Location: {city_name}, {county_name}"


message = get_location("Amarillo", "Potter")
print(message)


class Glossary:
    def __init__(definition, culicidae):
        definition.culicidae = culicidae
