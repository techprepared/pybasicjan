age = float(input())
what_gender = input()



if what_gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif what_gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
