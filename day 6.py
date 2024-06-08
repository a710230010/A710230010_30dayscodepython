from datetime import datetime

def main():
    # Meminta pengguna memasukkan tanggal dalam format yyyy-mm-dd
    tanggal_str = input("Masukkan tanggal (yyyy-mm-dd): ")

    try:
        # Mengonversi string input menjadi objek tanggal
        tanggal = datetime.strptime(tanggal_str, '%Y-%m-%d')

        # Mendapatkan nama hari dalam bahasa Indonesia
        hari_minggu = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        hari = hari_minggu[tanggal.weekday()]

        # Menampilkan hasil
        print(f"Tanggal {tanggal_str} adalah hari {hari}.")
    
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format yyyy-mm-dd.")

if __name__ == "__main__":
    main()
