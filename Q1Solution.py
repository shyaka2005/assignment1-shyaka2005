def findRent(start,end):
 def calculate_rate(start_time, end_time):
    
    time_slots = [
        (0, 7, 500),    # 0-7 hours rate: 500 RWF per hour
        (7, 10, 1000),  # 7-10 hours rate: 1000 RWF per hour
        (10, 19, 1500), # 10-19 hours rate: 1500 RWF per hour
        (19, 21, 1000), # 19-21 hours rate: 1000 RWF per hour
        (21, 24, 500)   # 21-24 hours rate: 500 RWF per hour
    ]
    
    
    if start_time < 0 or start_time >= 24 or end_time < 0 or end_time >= 24 or start_time > end_time:
        return "Invalid input"
    
    total_amount = 0
    current_time = start_time
    
    
    while current_time < end_time:
        for start, end, rate in time_slots:
           
            if current_time >= start and current_time < end:
                
                hours_in_this_slot = min(end_time, end) - current_time
                total_amount += hours_in_this_slot * rate
                current_time += hours_in_this_slot
                break  # Move to the next time range once we've handled the current range
    
    return total_amount

start_time = float(input("Enter the starting time (0-24): "))
end_time = float(input("Enter the ending time (0-24): "))


result = calculate_rate(start_time, end_time)
if result == "Invalid input":
    print(result)
else:
    print(f"The total amount to be paid is: {result} RWF")
      return 0

start=int(input("Enter start time"))
end=int(input("Enter end time"))
print(findRent(start,end))
