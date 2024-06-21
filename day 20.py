class MenuMakanan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def display_info(self):
        print(f"{self.nama}: Rp {self.harga:,.2f}")

class Pesanan:
    def __init__(self):
        self.daftar_pesanan = []

    def tambah_pesanan(self, menu, jumlah):
        self.daftar_pesanan.append({"menu": menu, "jumlah": jumlah})

    def total_harga(self):
        total = 0
        for pesanan in self.daftar_pesanan:
            total += pesanan["menu"].harga * pesanan["jumlah"]
        return total

    def tampilkan_pesanan(self):
        print("\nDaftar Pesanan:")
        for index, pesanan in enumerate(self.daftar_pesanan, start=1):
            print(f"{index}. {pesanan['menu'].nama} ({pesanan['jumlah']} pcs)")

class Restoran:
    def __init__(self, nama):
        self.nama = nama
        self.menu_makanan = []

    def tambah_menu(self, menu):
        self.menu_makanan.append(menu)
        print(f"Menu {menu.nama} berhasil ditambahkan ke restoran {self.nama}.")

    def tampilkan_menu(self):
        print(f"\nMenu di Restoran {self.nama}:")
        for menu in self.menu_makanan:
            menu.display_info()


def main():
    print("Selamat datang di Program Manajemen Restoran")

    # Membuat objek Restoran
    restoran = Restoran("Santapan Bahagia")

    # Membuat objek-objek MenuMakanan
    menu1 = MenuMakanan("Nasi Goreng", 25000)
    menu2 = MenuMakanan("Ayam Goreng", 30000)
    menu3 = MenuMakanan("Es Teh Manis", 5000)

    # Menambahkan menu ke restoran
    restoran.tambah_menu(menu1)
    restoran.tambah_menu(menu2)
    restoran.tambah_menu(menu3)

    # Menampilkan menu restoran
    restoran.tampilkan_menu()

    # Membuat objek Pesanan
    pesanan = Pesanan()

    # Memilih menu dan menambahkan ke pesanan
    pesanan.tambah_pesanan(menu1, 2)
    pesanan.tambah_pesanan(menu2, 1)
    pesanan.tambah_pesanan(menu3, 3)

    # Menampilkan pesanan dan total harga
    pesanan.tampilkan_pesanan()
    total = pesanan.total_harga()
    print(f"\nTotal harga pesanan: Rp {total:,.2f}")

    print("\nTerima kasih, silakan menikmati hidangan Anda di restoran kami!")


if __name__ == "__main__":
    main()
