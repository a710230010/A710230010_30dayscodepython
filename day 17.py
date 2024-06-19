class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = {}  # dictionary untuk menyimpan nilai

    def input_nilai(self, mata_kuliah, nilai):
        self.nilai[mata_kuliah] = nilai

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"NiM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print("Nilai:")
        for mata_kuliah, nilai in self.nilai.items():
            print(f"- {mata_kuliah}: {nilai}")


def main():
    print("Selamat datang di Program Data Mahasiswa")

    # Input data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan mahasiswa: ")

    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa(nama, nim, jurusan)

    # Input nilai mata kuliah
    while True:
        mata_kuliah = input("Masukkan nama mata kuliah (kosongkan untuk selesai): ")
        if mata_kuliah == "":
            break
        nilai = input(f"Masukkan nilai untuk {mata_kuliah}: ")
        mahasiswa1.input_nilai(mata_kuliah, nilai)

    # Menampilkan informasi mahasiswa dan nilai
    print("\nInformasi Mahasiswa:")
    mahasiswa1.display_info()

    print("\nTerima kasih, program telah selesai.")


if __name__ == "__main__":
    main()
