print("|=======================================|")
print("|     Program Menampilkan Kalender      |")
print("|=======================================|")

import calendar

tahun = int(input("Masukkan Tahun: "))
bulan = int(input("Masukkan Bulan: "))
print()

print("Hasil")
print(calendar.month(tahun, bulan))