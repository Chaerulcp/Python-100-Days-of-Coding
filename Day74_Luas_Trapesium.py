# Meminta input panjang sisi atas, sisi bawah, dan tinggi dari pengguna
sisi_atas = float(input("Masukkan panjang sisi atas: "))
sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

# Menghitung luas trapesium menggunakan rumus di atas
luas = (sisi_atas + sisi_bawah) * tinggi / 2

# Menampilkan hasilnya ke layar
print("Luas trapesium adalah", luas)
