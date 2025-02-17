chicken_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15

chicken_menus_number = int(input())
fish_menus_number = int(input())
vegetarian_menu_number = int(input())

chicken_total = chicken_price * chicken_menus_number
fish_total = fish_menu_price * fish_menus_number
vegetarian_total = vegetarian_menu_price * vegetarian_menu_number

menus_total = chicken_total + fish_total + vegetarian_total

desert = 0.2 * menus_total
delivery_price = 2.50

grand_total = menus_total + desert + delivery_price

print(grand_total)
