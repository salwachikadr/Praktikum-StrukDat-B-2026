kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

    #a. perulangan
for nama, nilai in kumpulan_nilai:
    if nilai >= 75:
        print("Selamat", (nama), "Anda Lulus!")
    else:
        print("Maaf", (nama), "Anda harus remedial.")