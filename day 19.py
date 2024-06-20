class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, isbn):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.isbn = isbn
        self.dipinjam = False  # status buku dipinjam atau tidak

    def display_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"ISBN: {self.isbn}")
        if self.dipinjam:
            print("Status: Sedang dipinjam")
        else:
            print("Status: Tersedia")

    def pinjam(self):
        if not self.dipinjam:
            self.dipinjam = True
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang tidak tersedia untuk dipinjam.")

    def kembalikan(self):
        if self.dipinjam:
            self.dipinjam = False
            print(f"Buku '{self.judul}' berhasil dikembalikan.")
        else:
            print(f"Buku '{self.judul}' sudah tersedia.")

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan ke perpustakaan.")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

    def tampilkan_daftar_buku(self):
        print(f"\nDaftar Buku di Perpustakaan {self.nama}:")
        for buku in self.daftar_buku:
            buku.display_info()


def main():
    print("Selamat datang di Program Manajemen Perpustakaan")

    # Membuat objek Perpustakaan
    perpus = Perpustakaan("Universitas ABC")

    # Membuat objek-objek Buku
    buku1 = Buku("Python Programming", "John Doe", 2020, "978-1234567890")
    buku2 = Buku("Machine Learning for Beginners", "Jane Smith", 2021, "978-9876543210")

    # Menambahkan buku ke perpustakaan
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)

    # Menampilkan daftar buku di perpustakaan
    perpus.tampilkan_daftar_buku()

    # Meminjam dan mengembalikan buku
    buku1.pinjam()
    buku2.pinjam()
    buku2.kembalikan()

    # Menampilkan informasi setelah peminjaman dan pengembalian
    print("\nSetelah peminjaman dan pengembalian:")
    perpus.tampilkan_daftar_buku()

    print("\nTerima kasih, program telah selesai.")


if __name__ == "__main__":
    main()
