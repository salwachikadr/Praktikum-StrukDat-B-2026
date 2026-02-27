kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

    #matkul hanya kelas A
difference = kelas_A.difference(kelas_B)
print("Mata kuliah yang diambil oleh kelas A", kelas_A)
   
    #matkul sama
matkulsama = kelas_A.intersection(kelas_B) #matkul yang ada di kedua kelas
print(matkulsama) 
#atau
irisan = kelas_A & kelas_B
print(irisan)

    #matkul unik
matakuliah =kelas_A.union(kelas_B) #gabung matkul 2 kelas
print("seluruh mata kuliah yang diambil oleh kedua kelas",matakuliah) 
#atau
gabungan = kelas_A | kelas_B
print(gabungan)
