# Casting tipe data adalah merubah tipe data dari satu tipe ke tipe lain

#Casting tipe data int ke float, str(string), bool(boolean)
# Data Awal
print("++++++++ int +++++++")
data_int = 100
print("Data = ",data_int, "Type data : ",type(data_int))

# Data setelah dicasting ke float
data_float = float(data_int)
print("Data = ",data_float, "Type data : ",type(data_float))

# Data setelah di casting ke str(string)
data_str = str(data_int)
print("Data = ",data_str, "Type data : ",type(data_str))

# Data setelah di casting ke bool(boolean)
data_bool = bool(data_int) # hasil casting akan false jika = 0
print("Data = ",data_bool, "Type data : ",type(data_bool))


#Casting tipe data float ke int, str(string), bool(boolean)
# Data Awal
print("++++++++ FLOAT +++++++")
data_float = 8.9
print("Data = ",data_float, "Type data : ",type(data_float))

# Data setelah dicasting ke int
data_int = int(data_float) # hasil casting float ke int nilainya akan di bulatkan ke bawah
print("Data = ",data_int, "Type data : ",type(data_int))

# Data setelah di casting ke str(string)
data_str = str(data_float)
print("Data = ",data_str, "Type data : ",type(data_str))

# Data setelah di casting ke bool(boolean)
data_bool = bool(data_float)
print("Data = ",data_bool, "Type data : ",type(data_bool))


#Casting tipe data bool(boolean) ke int, str(string), float
# Data Awal
print("++++++++ Boolean +++++++")
data_bool = True
print("Data = ",data_bool, "Type data : ",type(data_bool))

# Data setelah dicasting ke int
data_int = int(data_bool) # hasil casting boolean ke int akan 1 jika true dan 0 jika false
print("Data = ",data_int, "Type data : ",type(data_int))

# Data setelah di casting ke str(string)
data_str = str(data_bool) # hasil casting boolean ke str akan true jika true begitu pun sebaliknya
print("Data = ",data_str, "Type data : ",type(data_str))

# Data setelah di casting ke float
data_float = float(data_bool) # hasil casting boolean ke float akan 1 jika true dan 0 jika false
print("Data = ",data_float, "Type data : ",type(data_float))


#Casting tipe data str(string) ke int, bool(boolean), float
# Data Awal
print("++++++++ String +++++++")
data_str = "20"
print("Data = ",data_str, "Type data : ",type(data_str))

# Data setelah dicasting ke int
data_int = int(data_str) # data str harus angka agar bisa di casting
print("Data = ",data_int, "Type data : ",type(data_int))

# Data setelah di casting ke bool(boolean)
data_bool = bool(data_str) # hasil casting akan false jika nilai str kosong 
print("Data = ",data_bool, "Type data : ",type(data_bool))

# Data setelah di casting ke float
data_float = float(data_str) # data str harus angka agar bisa di casting
print("Data = ",data_float, "Type data : ",type(data_float))
