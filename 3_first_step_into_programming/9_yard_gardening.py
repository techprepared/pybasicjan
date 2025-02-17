square_meters_to_be_greened = float(input())

square_meter_price = 7.61
discount_from_company = 0.18



print(f"The final price is: {(square_meters_to_be_greened * square_meter_price) * (1 - discount_from_company)} lv.")
print(f"The discount is: {square_meters_to_be_greened * square_meter_price * discount_from_company} lv.")