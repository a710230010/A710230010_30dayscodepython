def main():
    daftar_tugas = []

    while True:
        print("\n1. Tambah Tugas\n2. Lihat Daftar Tugas\n3. Hapus Tugas\n4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tugas = input("Masukkan tugas: ")
            daftar_tugas.append(tugas)
            print(f"Tugas '{tugas}' ditambahkan.")
        elif pilihan == "2":
            if not daftar_tugas:
                print("Daftar tugas kosong.")
            else:
                for i, tugas in enumerate(daftar_tugas, start=1):
                    print(f"{i}. {tugas}")
        elif pilihan == "3":
            try:
                nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                if 1 <= nomor <= len(daftar_tugas):
                    print(f"Tugas '{daftar_tugas.pop(nomor - 1)}' dihapus.")
                else:
                    print("Nomor tugas tidak valid.")
            except ValueError:
                print("Masukkan nomor tugas yang valid.")
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
