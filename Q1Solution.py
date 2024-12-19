def findRent(start,end):
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

      return 0

start=int(input("Enter start time"))
end=int(input("Enter end time"))
print(findRent(start,end))
