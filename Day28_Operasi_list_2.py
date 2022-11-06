data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["alfin","asraf","darwin","adit"]

print(f"data = {data}")

index_darwin = data.index("darwin")
index_adit = data.index("adit")
print(f"index si darwin = {index_darwin}")
print(f"index si adit = {index_adit}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")