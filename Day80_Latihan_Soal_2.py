# Soal

# Buatlah program yang dapat menghitung total penjumlahan jika batas nilai atas diketahui. Nilai batas atas dimasukkan menggunakan fungsi input.
# Contoh nilai batas atas adalah 10 berarti
# 1+2+3+4+5+6+7+8+9+10 = 55


# Meminta input batas nilai atas dari pengguna
batas_atas = int(input("Masukkan batas nilai atas: "))

# Menghitung total penjumlahan dengan menggunakan loop for
total = 0
for i in range(1, batas_atas+1):
    total += i

# Menampilkan total penjumlahan ke layar
print("Total penjumlahan:", total)

