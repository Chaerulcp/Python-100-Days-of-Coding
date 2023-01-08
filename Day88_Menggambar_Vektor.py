import matplotlib.pyplot as plt

# Buat figure dan axis
fig, ax = plt.subplots()

# Buat vektor (x, y)
x = [1, 2]
y = [3, 4]

# Gambar vektor menggunakan function quiver
ax.quiver(0, 0, x, y, scale=1, angles='xy', scale_units='xy')

# Tambahkan label pada sumbu x dan y
ax.set_xlabel('Sumbu x')
ax.set_ylabel('Sumbu y')

# Tampilkan plot
plt.show()
