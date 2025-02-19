city = input()
volume_sales = float(input())
comission = 0

if city == "Sofia":
    if 0 < volume_sales <=500:
        comission = 0.05
    elif 500 < volume_sales <= 1000:
        comission = 0.07
    elif 1000 < volume_sales <= 10000:
        comission = 0.08
    elif volume_sales > 10000:
        comission = 0.12
elif city == "Varna":
    if 0 < volume_sales <=500:
        comission = 0.045
    elif 500 < volume_sales <= 1000:
        comission = 0.075
    elif 1000 < volume_sales <= 10000:
        comission = 0.10
    elif volume_sales > 10000:
        comission = 0.13
    else:
        comission = "unset"
elif city == "Plovdiv":
    if 0 < volume_sales <= 500:
        comission = 0.055
    elif 500 < volume_sales <= 1000:
        comission = 0.08
    elif 1000 < volume_sales <= 10000:
        comission = 0.12
    elif volume_sales > 10000:
        comission = 0.145
    else:
        comission = "unset"
else:
    city = "unset"

if city == "unset" or comission == "unset":
    print("error")
else:
    print(f"{volume_sales*comission:.2f}")