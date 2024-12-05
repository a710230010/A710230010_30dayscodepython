def efek_samping_jenis_sampah():
    # Dictionary untuk menyimpan efek samping berdasarkan jenis sampah
    efek_samping = {
        "organik": "Sampah ini mudah terurai, tetapi jika dibiarkan terlalu lama dapat menghasilkan bau busuk dan gas metana.",
        "anorganik": "Sampah ini sulit terurai dan dapat mencemari lingkungan jika tidak dikelola dengan baik.",
        "B3": "Sampah ini berbahaya dan dapat menyebabkan kerusakan lingkungan atau kesehatan jika tidak dibuang dengan benar.",
        "elektronik": "Sampah elektronik mengandung bahan berbahaya seperti merkuri dan timbal yang dapat mencemari tanah dan air.",
    }

    # Meminta input dari pengguna
    print("Jenis-jenis sampah yang tersedia: Organik, Anorganik, B3, Elektronik")
    jenis_sampah = input("Masukkan jenis sampah: ").strip().lower()

    # Mencocokkan input pengguna dengan efek samping
    if jenis_sampah in efek_samping:
        print(f"Jenis sampah: {jenis_sampah.capitalize()}")
        print(f"Efek samping: {efek_samping[jenis_sampah]}")
    else:
        print("Jenis sampah tidak dikenal. Harap masukkan jenis yang valid.")

# Menjalankan fungsi
efek_samping_jenis_sampah()
