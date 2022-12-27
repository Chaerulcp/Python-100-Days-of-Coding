# Soal

# Buatlah program yang mengetahui gaji bersih yang diterima karyawan setiap bulannya dengan ketentuan:
#  1. Gaji pokok masukkan melalui input
#  2. Gaji lembur/jam adalah Rp. 55.000
#  3. Lama lembur lembur dimasukkan melalui fungsi input()

# Meminta input gaji pokok dari pengguna
gaji_pokok = int(input("Masukkan gaji pokok: "))

# Meminta input lama lembur dari pengguna
lama_lembur = int(input("Masukkan lama lembur (jam): "))

# Menghitung gaji lembur dengan menggunakan gaji lembur per jam dan lama lembur yang diberikan
gaji_lembur = lama_lembur * 55000

# Menghitung gaji bersih dengan menambah gaji pokok dan gaji lembur
gaji_bersih = gaji_pokok + gaji_lembur

# Menampilkan gaji bersih ke layar
print("Gaji bersih:", gaji_bersih)

