# operator dictionary

data_dict = {
	"rul":"chaerul cp",
	"win":"darwin kabut",
	"han":"ramadhan loka"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "rul"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["rul"])
print(data_dict.get("rul"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["rul"] = "chaerul cp"
print(data_dict)
data_dict["win"] = "darwin kabut"
print(data_dict)

data_dict.update({"rul":"chaerul cp"})
print(data_dict)
data_dict.update({"irul":"chaerul cp"}) # kalau gak ada diadd ajah
print(data_dict)

# mendelete data pada dictionary
del data_dict["irul"]
print(data_dict)