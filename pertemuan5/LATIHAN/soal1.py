nilai_tugas = [70, 85, 90, 65, 80]

    #a. ganti nilai 65 menjadi 75
nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[3] = 75
print(nilai_tugas)

    #b. tambah nilai 95, lalu urutkan
nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas.append(95)
nilai_tugas.sort(reverse = True)
print(nilai_tugas)

    #c. jumlah total semua nilai
nilai_tugas = [70, 85, 90, 65, 80]
total = sum(nilai_tugas)
print(total)

    #d. tampilkan pesan
nilai_tugas = [70, 85, 90, 65, 80]
if 100 in nilai_tugas:
    print("Ada nilai sempurna")
else:
    print("Tidak ada")
