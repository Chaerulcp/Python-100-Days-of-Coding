## Operasi

# index   0(-3)  1(-2)  2(-1)
data = ["alfin","asraf","ramadhan"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_alfin = data[-3]
print(f"data alfin = {data_alfin}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"zabil")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("resma")
print(f"data ditambah lagi =\n{data}")

# menambah list dengan list
data_baru = ["darwin","adit","indra"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# merubah data
# kita ubah data 2 menjadi gibe
data[2] = "gibe"
print(f"data rubah = \n{data}")

# meremove data

data.remove("darwin")
print(f"data remove = \n{data}")
# data.remove("Darwin") akan error karena huruf harus sesuai yaitu "darwin"

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)