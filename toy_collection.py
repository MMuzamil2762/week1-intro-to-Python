toy_collection = {}

def add_toy(name, age_suitability, is_electronic):

    toy_collection[name] = {"age_suitability": age_suitability, "is_electronic": is_electronic}
    return toy_collection.get(name)

def find_toy(name):

    if name in toy_collection.keys():
        return toy_collection.get(name)
    else:
        return "Toy not found"

def remove_toy(name):

    print(toy_collection.pop(name))
    return name + " removed."

def list_toys():

    return toy_collection.keys()

