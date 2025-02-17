nylon_price = 1.50
paint_price = 14.50 # per liter
additive_price = 5.00 # per liter

nylon_needed = int(input())
paint_needed = int(input())
additive_needed = int(input())
hours_for_workers_needed = int(input())

nylon_total = (nylon_needed + 2) * nylon_price
paint_total = (paint_needed * 1.1) * paint_price
additive_total = additive_needed * additive_price
additional_expenses = 0.40

total_all_materials = nylon_total + paint_total + additive_total + additional_expenses

payment_for_workers = total_all_materials * 0.30 * hours_for_workers_needed

payment_total_material_and_workers = total_all_materials + payment_for_workers

print(payment_total_material_and_workers)