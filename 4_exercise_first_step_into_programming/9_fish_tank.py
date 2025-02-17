length = int(input())
width = int(input())
height = int(input())
percentage_for_equipment = float(input())

aquarius_in_cm3 = length * width * height
aquarius_in_dm3 = aquarius_in_cm3 / 1000

liters_needed = aquarius_in_dm3 * ( 1 - (percentage_for_equipment / 100))

print(liters_needed)

