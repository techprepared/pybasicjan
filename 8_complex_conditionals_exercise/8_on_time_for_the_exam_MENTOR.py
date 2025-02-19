MINUTES_IN_ONE_HOUR = 60

exam_hour = int(input())
exam_minutes = int(input())
arrived_hour = int(input())
arrived_minutes = int(input())

total_exam_minutes = (exam_hour * MINUTES_IN_ONE_HOUR) + exam_minutes
total_arrived_minutes = (arrived_hour * MINUTES_IN_ONE_HOUR) + arrived_minutes

time_diff = total_exam_minutes - total_arrived_minutes

time = ""

if time_diff > 30:
    time = "Early"
elif time_diff < 0:
    time = "Late"
else:
    print("On time")


hours = abs(time_diff) // MINUTES_IN_ONE_HOUR
minutes = abs(time_diff) % MINUTES_IN_ONE_HOUR

result = ""

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(time)
print(result)