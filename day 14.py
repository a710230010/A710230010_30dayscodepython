class Pasien:
    def __init__(self, nama, umur, alamat, no_hp):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.no_hp = no_hp

    def display_info(self):
        print(f"\nInformasi Pasien:")
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Alamat: {self.alamat}")
        print(f"No. HP: {self.no_hp}")


def main():
    print("Selamat datang di Layanan Pendaftaran Pasien")

    # Input data dari pengguna
    nama = input("Masukkan nama pasien: ")
    umur = input("Masukkan umur pasien: ")
    alamat = input("Masukkan alamat pasien: ")
    no_hp = input("Masukkan nomor HP pasien: ")

    # Membuat objek pasien
    pasien_baru = Pasien(nama, umur, alamat, no_hp)

    # Menampilkan informasi pasien yang telah terdaftar
    pasien_baru.display_info()

    print("\nTerima kasih, proses pendaftaran telah selesai.")


if __name__ == "__main__":
    main()
