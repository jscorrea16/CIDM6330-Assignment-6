# This is just my initial attempt to code my final project.
class Arthropod:
    def __init__(type, insect, arachnid):
        type.insect = insect
        type.arachnid = arachnid


class Geographical:
    def location(city_name, county_name):
        print(f"Location {city_name}, {county_name}")


location("Amarillo", "Potter")


class Glossary:
    def __init__(definition, culicidae):
        definition.culicidae = culicidae
