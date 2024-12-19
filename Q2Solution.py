def guess_mushroom():
    # Define the mushroom characteristics in a dictionary
    mushrooms = {
        "Agaric jaunissant": {"gills": True, "forest": False, "ring": True, "convex_cup": True},
        "Cepe de bordeaux": {"gills": False, "forest": True, "ring": False, "convex_cup": False},
        "Amanite tue-mouche": {"gills": True, "forest": True, "ring": True, "convex_cup": True},
        "Coprin chevelu": {"gills": True, "forest": False, "ring": True, "convex_cup": False},
        "Girolle": {"gills": True, "forest": True, "ring": False, "convex_cup": False},
        "Pied Bleu": {"gills": True, "forest": True, "ring": False, "convex_cup": True}
    }

    # Ask the user a maximum of three questions
    print("Please answer the following questions with 'yes' or 'no':")

    # Question 1: Does your mushroom have gills?
    q1 = input("Does your mushroom have gills? (yes/no): ").strip().lower()
    if q1 == "yes":
        possible_mushrooms = [name for name, attr in mushrooms.items() if attr["gills"]]
    elif q1 == "no":
        possible_mushrooms = [name for name, attr in mushrooms.items() if not attr["gills"]]
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return

    # If only one mushroom remains, we can stop early
    if len(possible_mushrooms) == 1:
        print(f"The mushroom you're thinking of is: {possible_mushrooms[0]}")
        return

    # Question 2: Does your mushroom grow in a forest?
    q2 = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower()
    if q2 == "yes":
        possible_mushrooms = [name for name in possible_mushrooms if mushrooms[name]["forest"]]
    elif q2 == "no":
        possible_mushrooms = [name for name in possible_mushrooms if not mushrooms[name]["forest"]]
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return

    # If only one mushroom remains, we can stop early
    if len(possible_mushrooms) == 1:
        print(f"The mushroom you're thinking of is: {possible_mushrooms[0]}")
        return

    # Question 3: Does your mushroom have a ring?
    q3 = input("Does your mushroom have a ring? (yes/no): ").strip().lower()
    if q3 == "yes":
        possible_mushrooms = [name for name in possible_mushrooms if mushrooms[name]["ring"]]
    elif q3 == "no":
        possible_mushrooms = [name for name in possible_mushrooms if not mushrooms[name]["ring"]]
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return

    # If after three questions only one mushroom is left, print the result
    if len(possible_mushrooms) == 1:
        print(f"The mushroom you're thinking of is: {possible_mushrooms[0]}")
    else:
        # If there are still multiple mushrooms, ask the fourth question (optional)
        q4 = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()
        if q4 == "yes":
            possible_mushrooms = [name for name in possible_mushrooms if mushrooms[name]["convex_cup"]]
        elif q4 == "no":
            possible_mushrooms = [name for name in possible_mushrooms if not mushrooms[name]["convex_cup"]]
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            return 

        if len(possible_mushrooms) == 1:
            print(f"The mushroom you're thinking of is: {possible_mushrooms[0]}")
        else:
            print("Could not determine the mushroom. Please check your answers.")

# Run the program
guess_mushroom
