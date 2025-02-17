number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days_to_read = int(input())

how_many_total_hours_needed = number_of_pages // pages_per_hour

how_many_hour_per_day_needed = how_many_total_hours_needed / number_of_days_to_read

print(int(how_many_hour_per_day_needed))