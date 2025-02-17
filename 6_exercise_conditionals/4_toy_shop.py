PUZZLE = 2.60
SPEAKING_DOLL = 3
BEAR = 4.10
MINION = 8.20
TRUCK = 2

excursion_price = float(input())
puzzle_count = int(input())
speaking_doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_total = PUZZLE * puzzle_count
speaking_doll_total = SPEAKING_DOLL * speaking_doll_count
bear_total = BEAR * bear_count
minion_total = MINION * minion_count
truck_total = TRUCK * truck_count

total_sales = puzzle_total + speaking_doll_total + bear_total + minion_total + truck_total

count_toys = puzzle_count + speaking_doll_count + bear_count + minion_count + truck_count

if count_toys >= 50:
    total_sales *= 0.75

total_sales *= 0.9 # expenses for the rent

if total_sales >= excursion_price:
    print(f"Yes! {total_sales-excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price-total_sales:.2f} lv needed.")
