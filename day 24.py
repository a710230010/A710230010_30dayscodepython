class Karyawan:
    def __init__(self, nama, usia, gaji):
        self.nama = nama
        self.usia = usia
        self.gaji = gaji

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Usia: {self.usia}, Gaji: ${self.gaji}")

    def naik_gaji(self, persentase):
        self.gaji *= (1 + persentase / 100)

# Membuat objek karyawan
karyawan1 = Karyawan("Alice", 25, 5000)
karyawan2 = Karyawan("Bob", 30, 6000)

# Menampilkan informasi karyawan
print("Informasi Karyawan:")
karyawan1.tampilkan_info()
karyawan2.tampilkan_info()

# Memberikan kenaikan gaji
karyawan1.naik_gaji(10)

# Menampilkan informasi karyawan setelah naik gaji
print("\nInformasi Karyawan setelah Naik Gaji:")
karyawan1.tampilkan_info()
karyawan2.tampilkan_info()
