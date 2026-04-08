from shapes import *

while True:
    print("\nSelect Shape:")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        break

    print("\nOperation:")
    print("1. Curved Surface Area")
    print("2. Total Surface Area")
    print("3. Volume")

    op = int(input("Enter operation: "))

    # Cube
    if choice == 1:
        a = float(input("Enter side: "))
        if op == 1:
            print("CSA =", cube_csa(a))
        elif op == 2:
            print("TSA =", cube_tsa(a))
        elif op == 3:
            print("Volume =", cube_volume(a))

    # Cuboid
    elif choice == 2:
        l = float(input("Length: "))
        b = float(input("Breadth: "))
        h = float(input("Height: "))
        if op == 1:
            print("CSA =", cuboid_csa(l, b, h))
        elif op == 2:
            print("TSA =", cuboid_tsa(l, b, h))
        elif op == 3:
            print("Volume =", cuboid_volume(l, b, h))

    # Cylinder
    elif choice == 3:
        r = float(input("Radius: "))
        h = float(input("Height: "))
        if op == 1:
            print("CSA =", cylinder_csa(r, h))
        elif op == 2:
            print("TSA =", cylinder_tsa(r, h))
        elif op == 3:
            print("Volume =", cylinder_volume(r, h))

    # Cone
    elif choice == 4:
        r = float(input("Radius: "))
        h = float(input("Height: "))
        l = float(input("Slant height: "))
        if op == 1:
            print("CSA =", cone_csa(r, l))
        elif op == 2:
            print("TSA =", cone_tsa(r, l))
        elif op == 3:
            print("Volume =", cone_volume(r, h))

    # Sphere
    elif choice == 5:
        r = float(input("Radius: "))
        if op == 1:
            print("CSA =", sphere_csa(r))
        elif op == 3:
            print("Volume =", sphere_volume(r))
        else:
            print("TSA same as CSA for sphere")

    else:
        print("Invalid choice")