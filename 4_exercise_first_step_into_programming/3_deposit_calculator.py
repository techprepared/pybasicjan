deposit_sum = float(input())
term_of_deposit = int(input())
year_percentage = float(input())/100

formula = deposit_sum + term_of_deposit * ((deposit_sum * year_percentage) / 12)

print(formula)