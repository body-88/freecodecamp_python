def add_time(start, duration, day):
    

    splitted_start= start.split(":")
    start_hours = int(splitted_start[0])
    splitted_minutes = splitted_start[1].split(" ")
    start_minutes = int(splitted_minutes[0])
    am_or_pm = splitted_minutes[1]
    flipping_am_and_pm = {
        "PM":"AM",
        "AM":"PM"
    }
    
    splitted_duration = duration.split(":")
    duration_hours = int(splitted_duration[0])
    splitted_duration_minutes = splitted_duration[1].split(" ")
    duration_minutes = int(splitted_duration_minutes[0])
    final_minutes = start_minutes + duration_minutes
    
    number_of_days = int(duration_hours / 24)
    
    if final_minutes >= 60:
        start_hours += 1
        final_minutes = final_minutes % 60
    final_hours = (start_hours + duration_hours) % 12
    number_of_flips = int((start_hours + duration_hours) / 12)
    
    if final_minutes > 9:
        final_minutes = final_minutes
    else:
        final_minutes = "0" + str(final_minutes)
    
    
    if final_hours == 0:
        final_hours = 12
    else:
        final_hours = final_hours
    
    
    if am_or_pm == "PM" and start_hours + (duration_hours % 12) >=12:
        number_of_days += 1 
        
    
    if number_of_flips % 2 == 1:
        am_or_pm = flipping_am_and_pm[am_or_pm]
    else:
        am_or_pm = am_or_pm
        
    
    result = f'{final_hours}:{final_minutes} {am_or_pm}'
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    
    if day:
        day_lower = day.lower()
        if day_lower in days:
            day_count = int(days.index(day_lower) + number_of_days) % 7
            changed_day = days[day_count].capitalize()
            result = f'{result}, {changed_day}'       

    
    if number_of_days == 1:
        return f'{result}, (next day)'
    elif number_of_days > 1:
        return f'{result} ({number_of_days} days later)'
    
    return  result


print(add_time("3:00 PM", "24:10", "Tuesday"))