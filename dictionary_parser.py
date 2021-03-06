import os
from json_handler import JSONHandler


def gather_meals_by_category(category: str):
    """
    When clicking on a category (breakfast, lunch, dinner, or dessert), we parse the entire meals.json for any meals
    with the appropriate category flag.

    :return: list of pairs containing key and Display Name for the meals found. i.e.:
     [[donut, Donut],
     [veggieOmelet, Veggie Omelet],
     [huevoRanchero, Huevo Ranchero]]
    """

    path = os.path.join(os.path.dirname(__file__), 'resources', 'meals.json')
    return_list = []

    # grab JSON to read - returns a dict
    json = JSONHandler(path)
    json_dict = json.read_json()

    for key, value in json_dict.items():
        if value[category] == 1:
            return_list.append([key, value["Display Name"]])

    return return_list


def gather_meals_by_search(search: str):
    """
    When searching for meals with a keyword we need to parse all meals for that keyword. Each meal should have relevant
    search terms in [key]["Search Terms"][list]

    :return: if no items are found that match, an empty list is returned.
    If items are found they are returned as a list of pairs containing key and Display Name for the meals found. i.e.:
     [[donut, Donut],
     [veggieOmelet, Veggie Omelet],
     [huevoRanchero, Huevo Ranchero]]
    """

    path = os.path.join(os.path.dirname(__file__), 'resources', 'meals.json')
    return_list = []

    # grab JSON to read - returns a dict
    json = JSONHandler(path)
    json_dict = json.read_json()

    for key, value in json_dict.items():
        for term in value["Search Terms"]:
            if term == search:
                return_list.append([key, value["Display Name"]])

    return return_list


def gather_ingredients_by_meal(meal: str):
    """
    Function to use for action where a meal has been selected and we need to gather a list of all the ingredients in the
    recipe
    :param meal: needs to be the key for the meal i.e. veggieOmelet
    :return: list of pairs that contain key, Display Name for all ingredients in the recipe. i.e.:
    [[milk, Milk],
    [sugar, White Sugar],
    [redPepper, Red Pepper]]
    """

    # TODO add in ethical alternative information into the return so that we can un-grey the symbols if its present.

    meal_path = os.path.join(os.path.dirname(__file__), 'resources', 'meals.json')
    ingredient_path = os.path.join(os.path.dirname(__file__), 'resources', 'ingredients.json')
    list_of_ingredients = []

    # grab meal JSON to read for specific meal
    meal_json = JSONHandler(meal_path)
    meal_json_dict = meal_json.read_json()
    recipe = meal_json_dict[meal]["Ingredients"]

    # grab ingredients JSON to read and then parse for ingredients in recipe
    ingredient_json = JSONHandler(ingredient_path)
    ingredient_json_dict = ingredient_json.read_json()

    for key in recipe:
        list_of_ingredients.append([[key], ingredient_json_dict[key]["Display Name"]])

    return list_of_ingredients


def gather_full_ingredient_list():
    """
    Function to return full list of ingredients specifically for the create recipe page.

    :return: list of pairs that contain key, Display Name for all ingredients in the recipe. i.e.:
    [[milk, Milk],
    [sugar, White Sugar],
    [redPepper, Red Pepper]]
    """

    ingredient_path = os.path.join(os.path.dirname(__file__), 'resources', 'ingredients.json')
    list_of_ingredients = []

    # grab ingredients JSON to read
    json = JSONHandler(ingredient_path)
    json_dict = json.read_json()

    for key, value in json_dict.items():
        list_of_ingredients.append([[key], json_dict[key]["Display Name"]])

    return list_of_ingredients
