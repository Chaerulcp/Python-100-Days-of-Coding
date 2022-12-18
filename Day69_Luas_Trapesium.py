# Program untuk menghitung luas trapesium

sisi_atas = float(input("Masukkan panjang sisi atas: "))
sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

luas = ((sisi_atas + sisi_bawah) * tinggi) / 2

print(f"Luas trapesium adalah {luas:.2f}")
