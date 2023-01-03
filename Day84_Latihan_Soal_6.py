# Soal

# Buatlah program yang dapat mengetahui penghasilan bersih tiap bulan seseorang dengan ketentuan sebagai berikut:
#  1. Jika Penghasilan minimal 3jt maka dikenakan pajak 5%
#  2. Jika penghasilan per bulan minimal 5jt maka dikenakan pajak 10%
#  3. Jika Jenis Pekerjaan adalah PNS maka Pajak ditambah 5%
#  4. Selain itu maka tidak kena pajak
#  5. Penghasilan dan Jenis Pekerjaan di input menggunakan fungsi input() pada python


# Meminta input penghasilan dari pengguna
penghasilan = int(input("Masukkan penghasilan per bulan: "))

# Meminta input jenis pekerjaan dari pengguna
jenis_pekerjaan = input("Masukkan jenis pekerjaan (PNS/Non-PNS): ")

# Menghitung pajak sesuai dengan ketentuan yang diberikan
if penghasilan >= 5000000:
  pajak = penghasilan * 0.1
elif penghasilan >= 3000000:
  pajak = penghasilan * 0.05
else:
  pajak = 0

# Jika jenis pekerjaan adalah PNS, menambahkan pajak sebesar 5%
if jenis_pekerjaan.lower() == "pns":
  pajak += penghasilan * 0.05

# Menghitung penghasilan bersih dengan mengurangi pajak dari penghasilan
penghasilan_bersih = penghasilan - pajak

# Menampilkan penghasilan bersih ke layar
print("Penghasilan bersih per bulan:", penghasilan_bersih)
