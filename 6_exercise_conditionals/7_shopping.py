budget = float(input())
video_cards = int(input())
processors = int(input())
ram_sticks = int(input())

video_cards_price = 250
video_cards_total = 250 * video_cards

processor_total = video_cards_total * 0.35 * processors
ram_stick_total = video_cards_total * 0.10 * ram_sticks

grand_total = video_cards_total + processor_total + ram_stick_total

if video_cards > processors:
    grand_total *= 0.85

if budget >= grand_total:
    print(f"You have {budget - grand_total:.2f} leva left!")
else:
    print(f"Not enough money! You need {grand_total-budget:.2f} leva more!")