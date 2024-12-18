def identify_mushroom():
    
    mushrooms = [
        {"name": "Agaric jaunissant", "gills": True, "forest": False, "ring": True, "convex_cup": True},
        {"name": "Cepe de bordeaux", "gills": False, "forest": True, "ring": False, "convex_cup": False},
        {"name": "Amanite tue-mouche", "gills": True, "forest": True, "ring": True, "convex_cup": True},
        {"name": "Coprin chevelu", "gills": True, "forest": False, "ring": True, "convex_cup": False},
        {"name": "Girolle", "gills": True, "forest": True, "ring": False, "convex_cup": False},
        {"name": "Pied Bleu", "gills": True, "forest": True, "ring": False, "convex_cup": True}
    ]
    
    # Ask the u
    gills_answer = input("Does your mushroom have gills? (yes/no): ").strip().lower()
    if gills_answer == "yes":
        mushrooms = [m for m in mushrooms if m["gills"]]
    else:
        mushrooms = [m for m in mushrooms if not m["gills"]]
    
    # If only one mushroom remains, we know the answer
    if len(mushrooms) == 1:
        print(f"Your mushroom is: {mushrooms[0]['name']}")
        return
    
    # Ask if it grows in a forest
    forest_answer = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower()
    if forest_answer == "yes":
        mushrooms = [m for m in mushrooms if m["forest"]]
    else:
        mushrooms = [m for m in mushrooms if not m["forest"]]
    
    # If only one mushroom remains, we know the answer
    if len(mushrooms) == 1:
        print(f"Your mushroom is: {mushrooms[0]['name']}")
        return
    
    # Ask if it has a ring
    ring_answer = input("Does your mushroom have a ring? (yes/no): ").strip().lower()
    if ring_answer == "yes":
        mushrooms = [m for m in mushrooms if m["ring"]]
    else:
        mushrooms = [m for m in mushrooms if not m["ring"]]
    
    # If only one mushroom remains, we know the answer
    if len(mushrooms) == 1:
        print(f"Your mushroom is: {mushrooms[0]['name']}")
        return
    
    # Ask if it has a convex cup
    convex_cup_answer = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower()
    if convex_cup_answer == "yes":
        mushrooms = [m for m in mushrooms if m["convex_cup"]]
    else:
        mushrooms = [m for m in mushrooms if not m["convex_cup"]]
    
    # Final answer
    if len(mushrooms) == 1:
        print(f"Your mushroom is: {mushrooms[0]['name']}")
    else:
        print("There seems to be an issue with the answers provided.")

# Run the function to identify the mushroom
identify_mushroom()
