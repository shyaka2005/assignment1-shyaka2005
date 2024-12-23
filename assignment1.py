#You have a business of many bicycles that
 #people can rent. We assume that:
 #The rate per hour depends on the time 
#0f the day as 
# follows:0 - 7         and 21-24  the rate 
#is RWF 500 per hour 7-  10     and      19-21 the rate
#is  RWF 1000 per hour 10- 19 the rate is 1500 per hour 
#Write a python program that takes as 
#input the starting time and the ending time 
#(a) If the starting is greater than the
#ending time or the sarting time or ending
#time is out of the range 0-24, 
#then display invalid input
#(b) Print the total amount to be paid 
#by the renter.def calculate_rental_cost(start_time, end_time):
    # Check if the input times are validdef calculate_rental_cost(start_time, end_time):
    # Check if input times are valid
def calculate_rental_cost(start_time, end_time):
    # Check if the input times are valid
    if start_time < 0 or start_time > 24 or end_time < 0 or end_time > 24:
        print("Invalid input: Time must be between 0 and 24.")
        return
    if start_time > end_time:
        print("Invalid input: Starting time cannot be greater than ending time.")
        return

    total_cost = 0

    # Loop through each hour and calculate the cost for each hour
    for hour in range(start_time, end_time):
        if (0 <= hour < 7) or (21 <= hour < 24):  # Rate is RWF 500 per hour
            total_cost += 500
        elif (7 <= hour < 10) or (19 <= hour < 21):  # Rate is RWF 1000 per hour
            total_cost += 1000
        elif 10 <= hour < 19:  # Rate is RWF 1500 per hour
            total_cost += 1500

    # Output the total cost
    print(f"Total amount to be paid by the renter: RWF {total_cost}")


# Take input for starting and ending time
try:
    start_time = int(input("Enter the starting time (0-24): "))
    end_time = int(input("Enter the ending time (0-24): "))
    calculate_rental_cost(start_time, end_time)
except ValueError:
    print("Invalid input: Please enter integers for time.")


#We have six types of mushrooms : 
#Agaric jaunissant
#Cepe de bordeaux
#Amanite tue-mouche
#Coprin chevelu
#Girolle
#Pied Bleu
#The cepe bordeaux is the only 
#one to have pores, the other mushrooms
#having gills.
#Both coprin chevelu and agaric jaunissant 
#grow In meadows, other mushrooms grow 
#in forests
#The only mushrooms to have a convex cup 
#are agaric jaunissant,amanite tue-mouches,
#and pied bleu.
#The only mushrooms to have a ring are 
 # agaric jaunissant,amanite tue-mouches,
  #and coprin chevelu.
  #The User thinks of a mushroom (one of the six).
#The program asks at most three of the  
#following four questions.
#The User answers truthfully by yes or no
#$Based on the user’s answers, the program 
#determines the mushroom.
#The questions: 
#Does your mushroom have gills ?
#Does your mushroom grow in a forest ?
#Does your mushroom have a ring?
#Does your mushroom have a convex cup?
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
