yearly_basketball_fee = int(input())

shoes_price = yearly_basketball_fee * 0.6
basketball_clothes = shoes_price * 0.8
basketball_ball = basketball_clothes * 0.25
basketball_accessories = basketball_ball * 0.2

total = shoes_price + basketball_clothes + basketball_ball + basketball_accessories + yearly_basketball_fee

print(total)