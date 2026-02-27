sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

    #a. nama mahasiswa hadir dikdua sesi
hadirterus = sesi_pagi & sesi_siang
print('mahasiswa yang hadir dikedua sesi bernama ', hadirterus)

    #b. total hadir tanpa duplikat
semuanya = set(sesi_pagi) | set(sesi_siang)
print("Siswa yang hadir di hari itu yaitu : ", semuanya)

    #gabungan keduanya
sesi_hari_ini = set(sesi_pagi) | set(sesi_siang)
print(sesi_hari_ini)