mahasiswa = {
    "A001": 
    {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": 
    {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": 
    {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

    #mahasiswa ipk> 3,5
print("Mahasiswa dengan IPK di atas 3.5:")
for nim, value in mahasiswa.items() :
    if value["ipk"] > 3.5:
        print(value["nama"])

    #rata rata ipk mahasiswa
Total = 0          #menyimpan total IPK
hitung = 0          #menyimpan jumlah mahasiswa
for x in mahasiswa : 
    Total = Total + (mahasiswa[x]["ipk"])         #perulangan menjumlahkan IPK
    hitung = hitung + 1 
    rata = Total / hitung 
print (rata) 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    #tambah data baru
mahasiswa ["A004"] = {"nama": "salwa", "prodi": "Informatika", "ipk": 4.00} #tambah dict baru
print(mahasiswa) #menampilkan semua dict