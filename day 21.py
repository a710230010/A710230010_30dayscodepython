import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox


class AplikasiMahasiswa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Daftar Mahasiswa')
        self.setup_ui()

    def setup_ui(self):
        # Widget Label dan LineEdit untuk input nama mahasiswa
        self.label_nama = QLabel('Nama Mahasiswa:')
        self.input_nama = QLineEdit()

        # Tombol untuk menambahkan nama mahasiswa ke daftar
        self.tombol_tambah = QPushButton('Tambah')

        # ListWidget untuk menampilkan daftar nama mahasiswa
        self.list_daftar_mahasiswa = QListWidget()

        # Layout utama menggunakan VBox
        layout_utama = QVBoxLayout()
        layout_utama.addWidget(self.label_nama)
        layout_utama.addWidget(self.input_nama)
        layout_utama.addWidget(self.tombol_tambah)
        layout_utama.addWidget(self.list_daftar_mahasiswa)

        self.setLayout(layout_utama)

        # Menghubungkan tombol tambah dengan fungsi tambah_mahasiswa
        self.tombol_tambah.clicked.connect(self.tambah_mahasiswa)

    def tambah_mahasiswa(self):
        nama_mahasiswa = self.input_nama.text()
        if nama_mahasiswa:
            self.list_daftar_mahasiswa.addItem(nama_mahasiswa)
            self.input_nama.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Silakan masukkan nama mahasiswa terlebih dahulu.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AplikasiMahasiswa()
    window.show()
    sys.exit(app.exec_())
