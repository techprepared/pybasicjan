exam_hour = int(input())
exam_minute = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())
is_on_time = ""

total_minutes_exam = (exam_hour * 60) + (exam_minute)
total_minutes_arrival = (hour_arrival * 60) + (minutes_arrival)
time_difference = total_minutes_exam - total_minutes_arrival
if time_difference > 30:
    is_on_time = "Early"
elif 0 <= time_difference <= 30:
    is_on_time = "On time"
else:
    is_on_time = "Late"



if time_difference >= 60:
    print(is_on_time)
    if abs(time_difference % 60) < 10:
        print(f"{abs(time_difference // 60)}:0{abs(time_difference % 60)} hours before the start")
    else:
        print(f"{abs(time_difference // 60)}:{abs(time_difference % 60)} hours before the start")
elif 0 < time_difference < 60:
    print(is_on_time)
    print(f"{time_difference} minutes before the start")
elif time_difference == 0:
    print(is_on_time)
elif 0 > time_difference > -60:
    print(is_on_time)
    print(f"{abs(time_difference)} minutes after the start")
elif time_difference <= -60:    
    print(is_on_time)
    if abs(time_difference % 60) < 10:
        print(f"{abs(time_difference) // 60}:0{abs(time_difference) % 60} hours after the start")
    else:
        print(f"{abs(time_difference) // 60}:{abs(time_difference) % 60} hours after the start")


