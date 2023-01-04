# Soal

# Buatlah program yang dapat memprediksi keuntungan setiap tahun yang akan didapatkan 
# seorang investor jika ketentuan investasi sebagai berikut:
#  1. Keuntungan tiap tahun adalah 5% dari total investasi
#  2. Setiap keuntungan per tahun, dimasukkan menjadi tambahan modal investasi pada
#     tahun berikutnya
#  3. Modal awal dan lama investasi (dalam tahun) di input menggunakan fungsi input() di python


# Meminta input modal awal dari pengguna
modal_awal = int(input("Masukkan modal awal: "))

# Meminta input lama investasi dari pengguna
lama_investasi = int(input("Masukkan lama investasi (dalam tahun): "))

# Menghitung dan menampilkan keuntungan setiap tahun
for tahun in range(1, lama_investasi+1):
    keuntungan = modal_awal * 0.05
    modal_awal += keuntungan
    print("Keuntungan tahun", tahun, ":", keuntungan)
