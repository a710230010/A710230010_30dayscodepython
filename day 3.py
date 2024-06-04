print("|====================================|")
print("|     Program Sederhana Mencari      |")
print("|   Huruf Vokal Pada Kata/Kalimat    |")
print("|====================================|")

def hitung_huruf_vokal(kalimat):
  
  huruf_vokal = "aiueoAIUEO"
  jumlah_vokal = 0

  for huruf in kalimat:
    if huruf in huruf_vokal:
      jumlah_vokal += 1

  return jumlah_vokal

kalimat = input("Masukkan kalimat/kata: ")
jumlah_vokal = hitung_huruf_vokal(kalimat)

print(f"Jumlah huruf vokal dalam '{kalimat}' adalah: {jumlah_vokal}")

