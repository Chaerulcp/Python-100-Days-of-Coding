# Konversi string biner ke ASCII
binary_string = "0100000101100010011011000110110001101111"
ascii_string = ""

for i in range(0, len(binary_string), 8):
    ascii_string += chr(int(binary_string[i:i+8], 2))

print(ascii_string)  # Output: "Abcdef"
