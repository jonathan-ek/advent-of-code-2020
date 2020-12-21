from helper import get_input, flatten


def main():
    recipes_raw = [x[:-1].split(' (contains ', 1) for x in get_input(21).split('\n') if x]
    recipes = []
    all_allergens = set()
    for ingredients, allergens in recipes_raw:
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')
        recipes.append([ingredients, allergens])
        for a in allergens:
            all_allergens.add(a)
    possible_ingredients = []
    for a in all_allergens:
        ingredients_with_allergen = [ingredients for ingredients, allergens in recipes if a in allergens]
        possible_ingredients.append([a, list(set.intersection(*map(set, ingredients_with_allergen)))])

    allergens_mapping = {}
    while True:
        tmp = []
        for key, value in possible_ingredients:
            used_ingredients = [a_value for a_value in allergens_mapping.values()]
            ing_list = [x for x in value if x not in used_ingredients]
            if len(ing_list) == 1:
                allergens_mapping[key] = ing_list[0]
            else:
                tmp.append([key, value])
        possible_ingredients = tmp
        if len(possible_ingredients) == 0:
            break
    ans = [x[1] for x in sorted([[allergen, ingredient] for allergen, ingredient in allergens_mapping.items()], key=lambda x: x[0])]
    print(','.join(ans))


if __name__ == '__main__':
    main()
