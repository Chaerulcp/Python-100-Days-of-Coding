# Konversi satuan temperature

print("=== Program Konversi Temperatur ===")\

# Konversi celcius ke satuan lain
# input user
celcius = float(input("Masukan suhu celcius : "))

# Logic
#  Celcius ke Reamur
reamur = (4/5) * celcius

# Celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32

# Celcius ke Kelvin 
kelvin = celcius + 273

# Output
print("Suhu adalah : ", celcius, "Celcius")
print("Suhu dalam reamur adalah : ", reamur, "Reamur")
print("Suhu dalam fahrenheit adalah : ", fahrenheit, "Fahrenheit")
print("Suhu dalam Kelvin adalah : ", kelvin, "Kelvin")
