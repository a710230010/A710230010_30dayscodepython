def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

# Angka yang ingin dihitung faktorialnya
angka = 5

# Menghitung faktorial
hasil = faktorial(angka)

# Menampilkan hasil
print(f"Faktorial dari {angka} adalah {hasil}")
