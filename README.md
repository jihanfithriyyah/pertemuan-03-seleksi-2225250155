# Pertemuan 03 Seleksi Python

Nama: Jihan Fithriyyah
NIM: 2225250155
Kelas: 3A

## Tujuan

Menulis program seleksi ataupun menjelaskan tujuan tugas, yaitu menggunakan if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan menuliskan perintah untuk menjalankan program-program Python.

```bash
python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
python tugas/analisis_persamaan_kuadrat.py
```

## Algoritma Tugas

Program dimulai dengan memasukkan nilai a, b, dan c. Selanjutnya, nilai a diperiksa terlebih dahulu. Jika a = 0, maka persamaan tersebut bukan persamaan kuadrat. Jika a ≠ 0, program menghitung nilai diskriminan dengan rumus D = b² − 4ac. Setelah itu, program menentukan jenis akar berdasarkan nilai D. Jika D > 0, terdapat dua akar real berbeda. Jika D = 0, terdapat satu akar real kembar. Jika D < 0, persamaan tidak memiliki akar real.

## Hasil Pengujian

| No | Input (a,b,c) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|---|
| 1 | (1,-5,6) | D = 1, dua akar real | D = 1, x1 = 3.00, x2 = 2.00 | Berhasil |
| 2 | (1,2,1) | D = 0, satu akar real kembar | D = 0, x = -1.00 | Berhasil |
| 3 | (1,0,1) | D = -4, tidak memiliki akar real | D = -4, tidak memiliki akar real | Berhasil |
| 4 | (0,2,3) | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Berhasil |

## Refleksi

Saat mengerjakan program, saya memahami bahwa setiap kondisi harus diperiksa dengan urutan yang tepat. Salah satu hal yang perlu diperhatikan adalah membedakan kondisi D > 0, D = 0, dan D < 0. Saya memperbaikinya dengan menggunakan nested if agar setiap kondisi dapat menghasilkan keluaran yang sesuai.