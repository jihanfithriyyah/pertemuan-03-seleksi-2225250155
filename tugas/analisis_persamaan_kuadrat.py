# Program analisis persamaan kuadrat
# Bentuk persamaan: ax^2 + bx + c = 0
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
if a == 0:
    print("Bukan persamaan kuadrat")
else:
    D = b**2 - 4*a*c
    print(f"Diskriminan (D) = {D:.2f}")
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print("Persamaan memiliki dua akar real berbeda")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    else:
        if D == 0:
            x = -b / (2*a)
            print("Persamaan memiliki satu akar real kembar")
            print(f"x = {x:.2f}")
        else:
            print("Persamaan tidak memiliki akar real")