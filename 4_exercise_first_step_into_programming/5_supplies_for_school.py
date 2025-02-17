pens_price = 5.80
markers_price = 7.20
detergent_per_liter_price = 1.20

packets_pens = int(input())
packets_markers = int(input())
detergent_liters = int(input())
discount = int(input())

pens_total = pens_price * packets_pens
markers_total = markers_price * packets_markers
detergent_total = detergent_per_liter_price * detergent_liters

sum_without_discount = pens_total + markers_total + detergent_total

total_sum = sum_without_discount * (1 - (discount / 100))

print(total_sum)

