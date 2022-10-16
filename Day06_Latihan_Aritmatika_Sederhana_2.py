# Kalkulator sederhana dengan input nilai dari user
# penjumlahan ( + ) 
# pengurangan (-) 
# pembagian ( / ) 
# perkalian ( * )
# modulus ( % )
# eksponen ( ** )

print("KALKULATOR ( +, -, *, /, % , ** )")

a = int(input("Nialai a = "))
b = int(input("Nialai b = "))
print("==========================\n")
# penjumlahan
hasil = a + b
print(a, '+', b,'=',hasil)

# pengurangan
hasil = a - b
print(a, '-', b,'=',hasil)

# perkalian
hasil = a * b
print(a, 'x', b,'=',hasil)

# pembagian
hasil = a / b
print(a, '/', b,'=',hasil)

# Modulus
hasil = a % b
print(a, '%', b,'=',hasil)

# eksponen ( pangkat )
hasil = a ** b
print(a, '**', b,'=',hasil)
