# Program menentukan jenis segitiga
a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))
# Memeriksa apakah ketiga sisi dapat membentuk segitiga
if a + b > c and a + c > b and b + c > a:
    
    # Menentukan jenis segitiga
    if a == b:
        if b == c:
            print("Segitiga sama sisi")
        else:
            print("Segitiga sama kaki")
    else:
        if a == c:
            print("Segitiga sama kaki")
        else:
            if b == c:
                print("Segitiga sama kaki")
            else:
                print("Segitiga sembarang")
else:
    print("Bukan segitiga")