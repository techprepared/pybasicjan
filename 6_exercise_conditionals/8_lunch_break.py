from math import ceil

name_of_series = input()
length_of_episode = int(input())
length_of_break = int(input())

time_for_lunch = length_of_break * 0.125
time_for_break = length_of_break * 0.25

remaining_time = length_of_break - time_for_break - time_for_lunch

if remaining_time >= length_of_episode:
    print(f"You have enough time to watch {name_of_series} and left with {ceil(remaining_time - length_of_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(length_of_episode - remaining_time)} more minutes.")

