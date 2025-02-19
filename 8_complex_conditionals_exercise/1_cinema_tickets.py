projection = input()
rows = int(input())
cols = int(input())
price = 0

total_seats = rows * cols

if projection == "Premiere":
    price = 12
elif projection == "Normal":
    price = 7.50
elif projection == "Discount":
    price = 5.00

print(f"{price * total_seats:.2f}")