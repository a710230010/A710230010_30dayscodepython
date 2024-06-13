def adalah_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Angka maksimal N
N = 30

# Membuat daftar bilangan prima hingga N
bilangan_prima = [x for x in range(2, N+1) if adalah_prima(x)]

# Menampilkan hasil
print(f"Bilangan prima hingga {N}:", bilangan_prima)
