budget = float(input())
season = input()
type_holiday = ""
accomodation = 0
destination = ""

if season == "summer":
    type_holiday = "Camp"
    if budget <= 100:
        accomodation = budget * 0.3
        destination = "Bulgaria"
    elif budget <= 1000:
        accomodation = budget * 0.4
        destination = "Balkans"
    else:
        accomodation = budget * 0.9
        destination = "Europe"
        type_holiday = "Hotel"
elif season == "winter":
    type_holiday = "Hotel"
    if budget <= 100:
        accomodation = budget * 0.70
        destination = "Bulgaria"
    elif budget <= 1000:
        accomodation = budget * 0.8
        destination = "Balkans"
    else:
        accomodation = budget * 0.9
        destination = "Europe"


print(f"Somewhere in {destination}", sep="")
print(f"{type_holiday} - {accomodation:.2f}")


