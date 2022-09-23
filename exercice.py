#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list[str | float] = None) -> list:
    if values is None:
        values = []
        while len(values) < 10:
            value = input("Entrez une valeur (type: int | float | str): ")
            try:
                # Try to convert to float,
                # will work if int or float, positive or negative (-)
                # Raising ValueError if it is a str
                value = float(value)
                if value.is_integer():
                    # Reassign to casted int
                    value = int(value)
            except ValueError:  # it is a string, don't reassign it
                pass

            values.append(value)

    # Convert floats to strings to compare them
    values.sort(key=str)

    return values


def anagrams(words: list[str] = None) -> bool:
    if words is None:
        words = []
        while (curr_len := len(words)) < 2:
            words.append(input(f"Entrez un mot #{curr_len + 1} à comparer : "))

    letter_counts: list[dict[str, int]] = []

    for word in words:
        l_count = {}
        for char in word:
            l_count[char] = l_count.get(char, 0) + 1

        letter_counts.append(l_count)

    return letter_counts[0] == letter_counts[1]


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))


def best_grades(student_grades: dict[str, list[float]]) -> dict[str, float]:
    best_student: tuple[str, float] = ("", 0)

    for student, grades in student_grades.items():
        if (avg := sum(grades) / len(grades)) > best_student[1]:
            best_student = (student, avg)

    return {best_student[0]: best_student[1]}


def frequence(sentence: str) -> dict:
    letter_count: dict[str, int] = {}
    for char in sentence:
        letter_count[char] = letter_count.get(char, 0) + 1

    # Reverse sort by value
    sorted_count: list[tuple[str, int]] = sorted(
        letter_count.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    for char, freq in sorted_count:
        if freq >= 5:
            print(f"{char}: {freq}")

    return letter_count


def get_recipe() -> tuple[str, list[str]]:
    name = input("Nom de la recette : ")
    ingredients: list[str] = []
    while True:
        if ingredients:
            print("Les ingrédients actuels sont : " + ", ".join(ingredients))
            choice = input("Souhaitez-vous ajouter un autre ingrédient? (O)ui/(N)on ")
            if choice.lower() == "n":
                break
        else:
            print("La liste d'ingrédients est vide")

        ingredients.append(input("Nom de l'ingrédient : "))

    return name, ingredients


def get_recipes() -> dict[str, list[str]]:
    recipes = {}
    while True:
        if recipes:
            print("Les recettes enregistrées sont : " + ", ".join(recipes.keys()))
            choice = input("Souhaitez-vous ajouter une autre recette? (O)ui/(N)on ")
            if choice.lower() == "n":
                break

        name, ingredients = get_recipe()
        recipes[name] = ingredients

    return recipes


def print_recipe(recipes: dict[str, list[str]]):
    while True:
        recipe = input("Quelle recette souhaitez-vous afficher? ")

        if recipe in recipes.keys():
            break
        else:
            print("Cette recette n'existe pas dans la base de donnée")
            print(
                "Veuillez choisir une des options suivantes :\n"
                + "\n".join([f"\t- {n}" for n in recipes.keys()])
            )

    print(f"Les ingrédients de {recipe} sont :")
    print("\n".join([f"\t- {ing}" for ing in recipes[recipe]]))


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(
        f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}"
    )

    sentence = (
        "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    )
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == "__main__":
    main()
