import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class AudioPlayerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Pemutar Audio')
        self.setup_ui()

    def setup_ui(self):
        # Label untuk menampilkan status pemutaran
        self.label_status = QLabel('Tidak ada file yang dipilih')

        # Tombol untuk memilih file audio
        self.tombol_pilih = QPushButton('Pilih Audio')
        self.tombol_pilih.clicked.connect(self.pilih_audio)

        # Tombol untuk memutar atau menghentikan pemutaran audio
        self.tombol_putar = QPushButton('Putar')
        self.tombol_putar.setEnabled(False)
        self.tombol_putar.clicked.connect(self.putar_audio)

        # Layout menggunakan VBox
        layout_utama = QVBoxLayout()
        layout_utama.addWidget(self.label_status)
        layout_utama.addWidget(self.tombol_pilih)
        layout_utama.addWidget(self.tombol_putar)

        self.setLayout(layout_utama)

        # Objek QMediaPlayer untuk memainkan audio
        self.player = QMediaPlayer()

    def pilih_audio(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter('Audio (*.mp3 *.wav)')
        file_dialog.selectFile('')
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.label_status.setText(f'File dipilih: {file_path}')
            self.tombol_putar.setEnabled(True)

    def putar_audio(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.tombol_putar.setText('Putar')
        else:
            self.player.play()
            self.tombol_putar.setText('Pause')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    audio_player = AudioPlayerApp()
    audio_player.show()
    sys.exit(app.exec_())
