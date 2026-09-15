# Program membandingkan dua bilangan
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
if a >= b:
    if a == b:
        print("Kedua bilangan sama")
    else:
        print("Bilangan pertama lebih besar")
else:
    print("Bilangan kedua lebih besar")