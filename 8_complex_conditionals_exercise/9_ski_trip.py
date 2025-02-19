day_for_trip = int(input()) - 1
type_of_place = input()
assessment = input()


discount = 0
place = 1

if day_for_trip < 10:
    if type_of_place == "room for one person":
        place = 18
        discount = 0
    elif type_of_place == "apartment":
        place = 25
        discount = 0.3
    elif type_of_place == "president apartment":
        discount = 0.1
        place = 35
elif 10 <= day_for_trip <= 15:
    if type_of_place == "room for one person":
        place = 18
        discount = 0
    elif type_of_place == "apartment":
        discount = 0.35
        place = 25
    elif type_of_place == "president apartment":
        discount = 0.15
        place = 35
elif day_for_trip > 15:
    if type_of_place == "room for one person":
        place = 18
        discount = 0
    elif type_of_place == "apartment":
        discount = 0.5
        place = 25
    elif type_of_place == "president apartment":
        discount = 0.20
        place = 35


total = (place * day_for_trip) - (place * day_for_trip * discount)

if assessment == "positive":
    total *= 1.25
elif assessment == "negative":
    total *= 0.9

print(f"{total:.2f}")