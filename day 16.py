class NomorTelepon:
    def __init__(self, nomor, aktif=False):
        self.nomor = nomor
        self.aktif = aktif

    def aktifkan(self):
        self.aktif = True
        print(f"Nomor telepon {self.nomor} telah diaktifkan.")

    def nonaktifkan(self):
        self.aktif = False
        print(f"Nomor telepon {self.nomor} telah dinonaktifkan.")

    def status(self):
        if self.aktif:
            print(f"Nomor telepon {self.nomor} aktif.")
        else:
            print(f"Nomor telepon {self.nomor} tidak aktif.")


def main():
    print("Selamat datang di Layanan Aktivasi Nomor Telepon")

    nomor = input("Masukkan nomor telepon yang ingin diaktifkan: ")

    nomor_telepon = NomorTelepon(nomor)

    print("\nMenu:")
    print("1. Aktifkan nomor telepon")
    print("2. Nonaktifkan nomor telepon")
    print("3. Cek status nomor telepon")
    print("0. Keluar")

    while True:
        pilihan = input("\nPilih menu (1/2/3/0): ")

        if pilihan == '1':
            nomor_telepon.aktifkan()
        elif pilihan == '2':
            nomor_telepon.nonaktifkan()
        elif pilihan == '3':
            nomor_telepon.status()
        elif pilihan == '0':
            print("Terima kasih, program telah selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka yang sesuai.")


if __name__ == "__main__":
    main()
