movie_budget = float(input())
number_of_statists = int(input())
single_statists_clothes_money = float(input())
decoration_expenses = movie_budget * 0.1

budget_for_statists = number_of_statists * single_statists_clothes_money

if number_of_statists > 150:
    budget_for_statists *= 0.9

total_expenses = budget_for_statists + decoration_expenses

if total_expenses > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_expenses - movie_budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {movie_budget - total_expenses:.2f} leva left.")

