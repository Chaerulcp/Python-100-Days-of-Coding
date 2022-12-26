def add_item(name, price, items):
  """Tambahkan barang ke daftar barang."""
  items.append((name, price))

def remove_item(name, items):
  """Hapus barang dari daftar barang."""
  for i, item in enumerate(items):
    if item[0] == name:
      del items[i]
      return

def calculate_total(items):
  """Hitung total biaya barang-barang."""
  total = 0
  for item in items:
    total += item[1]
  return total

# Buat daftar kosong untuk menyimpan barang-barang.
items = []

while True:
  # Tanyakan kepada pengguna apa yang ingin mereka lakukan.
  action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'checkout' to checkout: ")

  if action == "add":
    # Tanyakan kepada pengguna nama barang dan harganya
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))

    # Tambahkan barang ke daftar.
    add_item(name, price, items)

  elif action == "remove":
    # Tanyakan kepada pengguna nama barang yang akan dihapus.
    name = input("Enter the name of the item to remove: ")

    # Hapus barang dari daftar
    remove_item(name, items)

  elif action == "checkout":
    # Hitung total biaya.
    total = calculate_total(items)

    # Cetak total dan keluar dari loop
    print("Total:", total)
    break

  else:
    # Jika pengguna memasukkan aksi yang tidak valid, cetak pesan kesalahan.
    print("Invalid action. Please try again.")
