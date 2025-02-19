budget = int(input())
season = input()
fisherman_number = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
    if fisherman_number <= 6:
        boat_rent *= 0.9
    elif 7 <= fisherman_number <= 11:
        boat_rent *= 0.85
    elif fisherman_number >= 12:
        boat_rent *= 0.75
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
    if fisherman_number <= 6:
        boat_rent *= 0.9
    elif 7 <= fisherman_number <= 11:
        boat_rent *= 0.85
    elif fisherman_number >= 12:
        boat_rent *= 0.75
elif season == "Winter":
    boat_rent = 2600
    if fisherman_number <= 6:
        boat_rent *= 0.9
    elif 7 <= fisherman_number <= 11:
        boat_rent *= 0.85
    elif fisherman_number >= 12:
        boat_rent *= 0.75

if fisherman_number % 2 == 0 and season != "Autumn":
    boat_rent *= 0.95

if budget >= boat_rent:
    print(f"Yes! You have {budget - boat_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_rent - budget:.2f} leva.")

