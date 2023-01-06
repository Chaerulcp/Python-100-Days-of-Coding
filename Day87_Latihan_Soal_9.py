# Soal

# Buatlah program yang dapat menerima 2 input angka dengan ketentuan sebagai berikut :
#  1. Jika penjumlahan kedua nilai adalah genap, maka tambahkan angka 1
#  2. Jika penjumlahan kedua adalah ganjil, maka jumlah ditambah 2


# Meminta input angka pertama dari pengguna
angka_pertama = int(input("Masukkan angka pertama: "))

# Meminta input angka kedua dari pengguna
angka_kedua = int(input("Masukkan angka kedua: "))

# Menghitung penjumlahan kedua angka
jumlah = angka_pertama + angka_kedua

# Menambahkan angka sesuai dengan ketentuan yang diberikan
if jumlah % 2 == 0:
    jumlah += 1
else:
    jumlah += 2

# Menampilkan hasilnya ke layar
print("Hasil:", jumlah)
