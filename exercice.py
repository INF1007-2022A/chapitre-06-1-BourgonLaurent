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
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


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
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == "__main__":
    main()
