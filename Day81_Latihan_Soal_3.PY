# Soal

# Buatlah program yang dapat menerima inputan bilangan dengan ketentuan sebagai berikut:
#  1. Jika nilai yang diinput adalah bilangan genap, 
#     maka program akan menampilkan pesan genap dan 
#     kemudian meminta user untuk memasukkan kembali angka.
#  2. Jika nilai yang diinput adalah ganjil, maka program akan 
#     menampilkan pesan “You and I, end” dan 
#     tidak menerima inputan angka lagi


while True:
# Meminta input bilangan dari pengguna
    bilangan = int(input("Masukkan bilangan: "))

# Mengecek apakah bilangan genap atau ganjil
    if bilangan % 2 == 0:
# Jika bilangan genap, menampilkan pesan "genap" dan meminta input kembali
        print("Genap")
    else:
# Jika bilangan ganjil, menampilkan pesan "You and I, end" dan menghentikan program
        print("You and I, end")
    break
