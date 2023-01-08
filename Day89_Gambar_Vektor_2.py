import matplotlib.pyplot as plt

# Buat figure dan axis
fig, ax = plt.subplots()

# Buat vektor-vektor yang akan diplot
x1 = [1, 2, 3]
y1 = [4, 5, 6]
x2 = [7, 8, 9]
y2 = [10, 11, 12]
x3 = [13, 14, 15]
y3 = [16, 17, 18]

# Gambar vektor-vektor tersebut menggunakan function quiver
ax.quiver(0, 0, x1, y1, scale=1, angles='xy', scale_units='xy')
ax.quiver(0, 0, x2, y2, scale=1, angles='xy', scale_units='xy')
ax.quiver(0, 0, x3, y3, scale=1, angles='xy', scale_units='xy')

# Tambahkan label pada sumbu x dan y
ax.set_xlabel('Sumbu x')
ax.set_ylabel('Sumbu y')

# Tampilkan plot
plt.show()
