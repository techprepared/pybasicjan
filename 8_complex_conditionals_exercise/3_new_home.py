ROSE = 5
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

flower = input()
quantity = int(input())
budget = float(input())
price = 0



if flower == "Roses":
    price = ROSE
    if quantity > 80:
        price = ROSE * 0.9
elif flower == "Dahlias":
    price = DAHLIA
    if quantity > 90:
        price = DAHLIA * 0.85
elif flower == "Tulips":
    price = TULIP
    if quantity > 80:
        price = TULIP * 0.85
elif flower == "Narcissus":
    price = NARCISSUS
    if quantity < 120:
        price = NARCISSUS * 1.15
elif flower == "Gladiolus":
    price = GLADIOLUS
    if quantity < 80:
        price = GLADIOLUS * 1.2

total_flowers = (quantity * price) 

if budget >= total_flowers:
    print(f"Hey, you have a great garden with {quantity} {flower} and {budget - total_flowers:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_flowers - budget:.2f} leva more.")