# Soal

# Buatlah program yang dapat menerima inputan berupa angka dengan ketentuan sebagai berikut:
#  1. Jika angka yang diinput habis dibagi 3, maka program akan mencetak pesan “Pride of 3”
#  2. Jika angka yang diinput habis dibagi 5, maka program akan mencetak pesan “Pride of 5”
#  3. Jika angka yang diinput habis dibagi 3 dan 5, maka program akan mencetak pesan “Master Class”


# Meminta input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Mengecek apakah angka habis dibagi 3, 5, atau keduanya
if angka % 3 == 0 and angka % 5 == 0:
    # Jika habis dibagi 3 dan 5, menampilkan pesan "Master Class"
    print("Master Class")
elif angka % 3 == 0:
    # Jika habis dibagi 3, menampilkan pesan "Pride of 3"
    print("Pride of 3")
elif angka % 5 == 0:
    # Jika habis dibagi 5, menampilkan pesan "Pride of 5"
    print("Pride of 5")
else:
    # Jika tidak habis dibagi 3 atau 5, menampilkan pesan "None of them"
    print("None of them")
