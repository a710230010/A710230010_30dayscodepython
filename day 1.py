# Inisialisasi daftar produk dan harga
daftar_produk = {"Apel": 5000, "Jeruk": 7000, "Pisang": 4000, "Melon": 10000}

# Fungsi untuk menampilkan daftar produk
def tampilkan_daftar_produk():
    print("Daftar Produk:")
    for produk, harga in daftar_produk.items():
        print(f"{produk}: Rp {harga}")

# Fungsi untuk menghitung total pembelian
def hitung_total_pembelian(pesanan):
    total = 0
    for item in pesanan:
        if item in daftar_produk:
            total += daftar_produk[item]
        else:
            print(f"Produk '{item}' tidak ada dalam daftar.")
    return total

# Fungsi utama
def main():
    tampilkan_daftar_produk()
    pesanan = input("Masukkan pesanan Anda (pisahkan dengan koma): ").split(",")
    total_pembelian = hitung_total_pembelian(pesanan)
    print(f"Total pembelian Anda: Rp {total_pembelian}")

if __name__ == "__main__":
    main()
0