# Soal

# Dilan ingin membeli Komputer sultan seharga 55jt. Gaji pokok Dilan perbulan adalah 5jt. 
# Setiap bulan Dilan harus membayar uang kost sebesar 750rb. Uang yang dapat ditabung dalam 
# sebulan maksimal 1,5jt. Sementara itu, Dilan juga harus memenuhi kebutuhan hidupnya sehari-hari.
# Buatlah program yang dapat membantu dilan untuk mengetahui minimal berapa bulan dia menabung
# untuk dapat membeli Komputer sultan.


# Harga Komputer sultan
harga_komputer = 55000000

# Gaji pokok Dilan per bulan
gaji_pokok = 5000000

# Uang yang dapat ditabung dalam sebulan
tabungan_maksimal = 1500000

# Biaya hidup sehari-hari Dilan
biaya_hidup = gaji_pokok - tabungan_maksimal - 750000

# Jumlah uang yang dibutuhkan Dilan untuk membeli Komputer sultan
uang_dibutuhkan = harga_komputer - biaya_hidup

# Menghitung minimal berapa bulan Dilan harus menabung untuk membeli Komputer sultan
bulan = uang_dibutuhkan // tabungan_maksimal

# Menampilkan hasilnya ke layar
print("Dilan harus menabung selama minimal", bulan, "bulan untuk dapat membeli Komputer sultan.")
