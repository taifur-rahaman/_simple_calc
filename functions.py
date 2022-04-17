def add():
    how_many = int(input("Enter how many number you want to add: "))
    total = 0
    numbers = []
    for i in range(how_many):
        number = float(input(f"Enter {i + 1} number: "))
        numbers.append(number)

    for number in numbers:
        total += number

    count = 0

    for i in numbers:
        print(i, end=" ")
        if count < how_many - 1:
            print("+", end=" ")
        count += 1
    print(" = " + str(total))


def sub():
    how_many = int(input("Enter how many number you want to subtract: "))
    total = 0
    numbers = []
    for i in range(how_many):
        number = float(input(f"Enter {i + 1} number: "))
        numbers.append(number)

    for number in numbers:
        total -= number

    count = 0

    for i in numbers:
        print(i, end=" ")
        if count < how_many - 1:
            print("-", end=" ")
        count += 1
    print(" = " + str(total))


def mul():
    how_many = int(input("Enter how many number you want to multiply: "))
    total = 0
    numbers = []
    for i in range(how_many):
        number = float(input(f"Enter {i + 1} number: "))
        numbers.append(number)

    for number in numbers:
        total *= number

    count = 0

    for i in numbers:
        print(i, end=" ")
        if count < how_many - 1:
            print("*", end=" ")
        count += 1
    print(" = " + str(total))


def div():
    a, b = map(float, input("Enter two number: ").split())
    print(f"{a} / {b} = {a / b:0.2f}")


def power():
    base = float(input("Enter the base: "))
    exp = float(input("Enter the exponent: "))
    print(f"{base} to the power {exp} is {base ** exp}")


def area():
    print("\n1. Circle\n2. Square\n3. Rectangle\n4. Triangle\n5. Trapezoid\n")
    choice = int(input("Enter your choice : "))

    while choice not in {1, 2, 3, 4, 5}:
        print("\nInvalid Input\n")
        print("\n1. Circle\n2. Square\n3. Rectangle\n4. Triangle\n5. Trapezoid\n")
        choice = int(input("Enter your choice : "))

    if choice == 1:
        pi = 3.14159
        radius = float(input("Enter the radius of the Circle: "))
        area_circle = pi * (radius ** 2)
        print(f"The area of the circle is {area_circle:0.2f}")
    elif choice == 2:
        side = float(input("Enter the side of the square: "))
        area_square = side ** 2
        print(f"The area of the square is {area_square:0.2f}")
    elif choice == 3:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area_rect = width * height
        print(f"The area of the rectangle is {area_rect:0.2f}")
    elif choice == 4:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area_triangle = 0.5 * base * height
        print(f"The area of the triangle is {area_triangle:0.2f}")
    elif choice == 5:
        base_1, base_2 = map(float, input("Enter the first and second base of the Trapezoid: "))
        height = float("Enter the height of the Trapezoid: ")
        area_trapezoid = ((base_1 + base_2) / 2) * height
        print(f"Enter the area of the Trapezoid is {area_trapezoid:0.2f}")


def vol():
    print("\n1. Cube\n2. Rectangular Prism\n3. Cylinder\n4. Cone\n5. Sphere\n")
    choice = int(input("Enter your choice : "))

    while choice not in {1, 2, 3, 4, 5}:
        print("\nInvalid Input\n")
        print("\n1. Cube\n2. Rectangular Prism\n3. Cylinder\n4. Cone\n5. Sphere\n")
        choice = int(input("Enter your choice : "))

    if choice == 1:
        radius = float(input("Enter the edge of the Cube: "))
        vol_cube = radius ** 3
        print(f"The volume of the cube is {vol_cube:0.2f}")
    elif choice == 2:
        length = float(input("Enter the length of the Prism: "))
        width = float(input("Enter the width of the Prism: "))
        height = float(input("Enter the height of the Prism: "))
        vol_prism = length * width * height
        print(f"The volume of the prism is {vol_prism:0.2f}")
    elif choice == 3:
        pi = 3.14159
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        vol_cylinder = pi * (radius ** 2) * height
        print(f"The volume of the cylinder is {vol_cylinder:0.2f}")
    elif choice == 4:
        pi = 3.14159
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        vol_cone = pi * (radius ** 2) * (height / 3)
        print(f"The volume of the cone is {vol_cone:0.2f}")
    elif choice == 5:
        pi = 3.14159
        radius = float("Enter the radius of the Sphere: ")
        vol_sphere = (4 / 3) * pi * (radius ** 3)
        print(f"Enter the volume of the Sphere is {vol_sphere:0.2f}")
