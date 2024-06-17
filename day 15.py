def tampilkan_menu():
    print("\nMenu Kasir Minimarket")
    print("1. Tambah Item")
    print("2. Lihat Keranjang")
    print("3. Hitung Total")
    print("4. Keluar")

def tambah_item(keranjang):
    nama_item = input("Masukkan nama item: ")
    try:
        harga_item = float(input("Masukkan harga item: "))
        jumlah_item = int(input("Masukkan jumlah item: "))
        keranjang.append({'nama': nama_item, 'harga': harga_item, 'jumlah': jumlah_item})
        print(f"Item '{nama_item}' sebanyak {jumlah_item} dengan harga {harga_item} berhasil ditambahkan.")
    except ValueError:
        print("Harga dan jumlah item harus berupa angka.")

def lihat_keranjang(keranjang):
    if not keranjang:
        print("Keranjang kosong.")
    else:
        print("\nDaftar Item di Keranjang:")
        for i, item in enumerate(keranjang, start=1):
            print(f"{i}. {item['nama']} - {item['jumlah']} x {item['harga']}")

def hitung_total(keranjang):
    total = sum(item['harga'] * item['jumlah'] for item in keranjang)
    print(f"\nTotal harga: {total:.2f}")

def main():
    keranjang = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            tambah_item(keranjang)
        elif pilihan == "2":
            lihat_keranjang(keranjang)
        elif pilihan == "3":
            hitung_total(keranjang)
        elif pilihan == "4":
            print("Terima kasih telah berbelanja. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
