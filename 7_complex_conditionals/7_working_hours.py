hour_of_the_day = int(input())
day_of_the_week = input()
is_it_open = ""
if 10 <= hour_of_the_day <= 18:
    if day_of_the_week == "Monday":
        is_it_open = "open"
    elif day_of_the_week == "Tuesday":
        is_it_open = "open"
    elif day_of_the_week == "Wednesday":
        is_it_open = "open"
    elif day_of_the_week == "Thursday":
        is_it_open = "open"
    elif day_of_the_week == "Friday":
        is_it_open = "open"
    elif day_of_the_week == "Saturday":
        is_it_open = "open"
    else:
        is_it_open = "closed"
else:
    is_it_open = "closed"

print(is_it_open)