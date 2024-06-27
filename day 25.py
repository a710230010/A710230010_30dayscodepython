import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QLineEdit, QMessageBox

class DaftarHadirApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Daftar Hadir Wedding')
        self.setup_ui()

    def setup_ui(self):
        # Label dan LineEdit untuk nama tamu
        self.label_nama = QLabel('Nama Tamu:')
        self.input_nama = QLineEdit()

        # Tombol untuk menambahkan tamu ke daftar hadir
        self.tombol_tambah = QPushButton('Tambahkan Tamu')
        self.tombol_tambah.clicked.connect(self.tambahkan_tamu)

        # ListWidget untuk menampilkan daftar hadir
        self.list_daftar_hadir = QListWidget()

        # Tombol untuk menghapus tamu yang dipilih
        self.tombol_hapus = QPushButton('Hapus Tamu')
        self.tombol_hapus.clicked.connect(self.hapus_tamu)

        # Layout menggunakan VBox dan HBox
        layout_utama = QVBoxLayout()
        layout_input = QHBoxLayout()
        layout_input.addWidget(self.label_nama)
        layout_input.addWidget(self.input_nama)
        layout_input.addWidget(self.tombol_tambah)
        layout_utama.addLayout(layout_input)
        layout_utama.addWidget(self.list_daftar_hadir)
        layout_utama.addWidget(self.tombol_hapus)

        self.setLayout(layout_utama)

    def tambahkan_tamu(self):
        nama_tamu = self.input_nama.text().strip()
        if nama_tamu:
            self.list_daftar_hadir.addItem(nama_tamu)
            self.input_nama.clear()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Masukkan nama tamu terlebih dahulu.')

    def hapus_tamu(self):
        index = self.list_daftar_hadir.currentRow()
        if index >= 0:
            self.list_daftar_hadir.takeItem(index)
        else:
            QMessageBox.warning(self, 'Peringatan', 'Pilih tamu yang akan dihapus.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    daftar_hadir_app = DaftarHadirApp()
    daftar_hadir_app.show()
    sys.exit(app.exec_())
