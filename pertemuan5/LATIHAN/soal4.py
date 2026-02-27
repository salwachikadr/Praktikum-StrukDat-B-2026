transaksi = [
    {"produk": "Buku", "harga": 10000, "jumlah": 3},
    {"produk": "Pena", "harga": 5000, "jumlah": 10},
    {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

    #a. Ubah jumlah buku
transaksi[0]["jumlah"] = 8
print(transaksi)

# Tambah 2 produk
transaksi.append({"produk": "Tipe_x", "harga": 8000, "jumlah": 5})
transaksi.append({"produk": "Penggaris", "harga": 4000, "jumlah": 4})
print(transaksi)

# Hitung total pendapatan
for i in transaksi:
    total = i["harga"] * i["jumlah"]
    print("Produk:", i["produk"], "| Total:", total)