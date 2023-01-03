# Soal

# Buatlah program yang dapat menerima inputan berupa angka dengan ketentuan sebagai berikut:
#  1. Angka yang dimasukkan melalui input adalah batas atas angka
#  2. Program menampilkan jumlah angka yang habis dibagi 3
#     Contoh angka yang diinput adalah 10, maka jawabannya adalah 3, 
#     karena ada 3 angka yang habis dibagi 3 yaitu 3, 6 dan 9


# Meminta input batas atas angka dari pengguna
batas_atas = int(input("Masukkan batas atas angka: "))

# Menghitung jumlah angka yang habis dibagi 3
jumlah = 0
for i in range(1, batas_atas+1):
    if i % 3 == 0:
        jumlah += 1

# Menampilkan jumlah angka yang habis dibagi 3 ke layar
print("Jumlah angka yang habis dibagi 3:", jumlah)
