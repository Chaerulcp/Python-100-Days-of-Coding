#program membuat beberapa segitiga dengan karakter bintang

jumlah = int(input("Masukkan jumlah baris :"))

print ("bentuk segitiga pertama dengan karakter bintang")
for i in range (jumlah+1):
    print ("*"*(jumlah-i))

print ("bentuk segitiga kedua dengan karakter bintang")
for i in range (jumlah+1):
    print ("*"*i)

print ("bentuk segitiga ketiga dengan karakter bintang")
for i in range (jumlah+1):
    print (" "*(jumlah-i),"*"*i)

print ("bentuk segitiga keempat dengan karakter bintang")
for i in range (jumlah+1):
    print (" "*(i),"*"*(jumlah-i))
