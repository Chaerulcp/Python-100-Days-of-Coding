# Break
angka = 0

while angka < 5:
	angka += 1
	print(f"angka sekarang = {angka}")

	if angka == 3:
		print("nice!")
		break

	print("hallo guys!")

print("finish!")

data_int = int(input("hitung sampai = "))

angka = 0

while True:
	angka += 1
	print(f"count = {angka}")

	if angka == data_int:
		print("nice!")
		break

	print("yooo guys!")

print("finish!")