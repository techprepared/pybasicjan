from math import pi

what_shape = input()

if what_shape == "square":
    one_side = float(input())
    print(f"{one_side**2:.3f}")
elif what_shape == "rectangle":
    width = float(input())
    height = float(input())
    face = width * height
    print(f"{face:.3f}")
elif what_shape == "circle":
    radius = float(input())
    print(f"{pi * radius**2:.3f}")
elif what_shape == "triangle":
    side = float(input())
    heigth_to_side = float(input())
    tr_face = 0.5 * side * heigth_to_side
    print(f"{tr_face:.3f}")
else:
    pass