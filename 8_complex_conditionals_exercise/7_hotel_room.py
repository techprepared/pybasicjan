month = input()
days = int(input())
apartment = 0
studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if days > 14:
        studio *= 0.7
    elif days > 7:
        studio *= 0.95
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio *= 0.8
elif month == "July" or month == "August":
    studio = 76
    apartment = 77


if days > 14:
    apartment *= 0.9

print(f"Apartment: {apartment * days:.2f} lv.", sep="")
print(f"Studio: {studio * days:.2f} lv.")

