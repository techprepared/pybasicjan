hours = int(input())
minutes = int(input())
added_time = 15

convert_everything_to_minutes = (hours * 60) + minutes + added_time

total_hours = convert_everything_to_minutes // 60
total_minutes = convert_everything_to_minutes - (total_hours * 60)

if total_hours % 24 == 0:
    total_hours = 0

if total_minutes < 10:
    print(f"{total_hours}:0{total_minutes}")
else:
    print(f"{total_hours}:{total_minutes}")





