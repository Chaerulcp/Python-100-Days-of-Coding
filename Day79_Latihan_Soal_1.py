# Soal

# Buatlah program yang dapat mengetahui berapa uang bersih yang didapatkan dari hasil penjualan tanah setelah dipotong pajak dengan ketentuan:
# 1. Harga Jual Permeter adalah Rp 300.000
# 2. Jika total harga jual 50 jt keatas maka dikenakan pajak 3%
# 3. Jika Total harga jual 100 jt keatas maka dikenakan pajak 5%
# 4. Dibawah 50jt maka dikenakan pajak 1%.
# 5. Luas tanah diinput menggunakan fungsi input pada python

# Meminta input luas tanah dari pengguna
luas_tanah = int(input("Masukkan luas tanah (meter persegi): "))

# Menghitung harga jual tanah dengan mengalikan harga jual per meter dengan luas tanah
harga_jual = luas_tanah * 300000

# Menghitung pajak sesuai dengan ketentuan yang diberikan
if harga_jual >= 100000000:
  pajak = harga_jual * 0.05
elif harga_jual >= 50000000:
  pajak = harga_jual * 0.03
else:
  pajak = harga_jual * 0.01

# Menghitung uang bersih dengan mengurangi harga jual dengan pajak
uang_bersih = harga_jual - pajak

# Menampilkan uang bersih ke layar
print("Uang bersih yang didapatkan:", uang_bersih)

