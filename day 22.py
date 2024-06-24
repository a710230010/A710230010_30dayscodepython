import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AplikasiHitungLuasSegitiga(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Hitung Luas Segitiga')
        self.setup_ui()

    def setup_ui(self):
        # Label dan LineEdit untuk input alas
        self.label_alas = QLabel('Alas:')
        self.input_alas = QLineEdit()

        # Label dan LineEdit untuk input tinggi
        self.label_tinggi = QLabel('Tinggi:')
        self.input_tinggi = QLineEdit()

        # Tombol untuk menghitung luas segitiga
        self.tombol_hitung = QPushButton('Hitung Luas')

        # Label untuk menampilkan hasil luas
        self.label_hasil = QLabel()

        # Layout utama menggunakan VBox
        layout_utama = QVBoxLayout()
        layout_utama.addWidget(self.label_alas)
        layout_utama.addWidget(self.input_alas)
        layout_utama.addWidget(self.label_tinggi)
        layout_utama.addWidget(self.input_tinggi)
        layout_utama.addWidget(self.tombol_hitung)
        layout_utama.addWidget(self.label_hasil)

        self.setLayout(layout_utama)

        # Menghubungkan tombol_hitung dengan fungsi hitung_luas_segitiga
        self.tombol_hitung.clicked.connect(self.hitung_luas_segitiga)

    def hitung_luas_segitiga(self):
        try:
            alas = float(self.input_alas.text())
            tinggi = float(self.input_tinggi.text())
            luas = 0.5 * alas * tinggi
            self.label_hasil.setText(f'Luas Segitiga: {luas:.2f}')
        except ValueError:
            QMessageBox.warning(self, 'Peringatan', 'Masukkan angka yang valid untuk alas dan tinggi.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AplikasiHitungLuasSegitiga()
    window.show()
    sys.exit(app.exec_())
