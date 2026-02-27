from tabulate import tabulate       #untuk buat tabel
from Kurs import kurs               #data kurs
from Konverter import konversi      #fungsi perhitungan

print("=== KONVERTER MATA UANG ===")        #menampilkan judul

# Menampilkan tabel kurs
data = []       #list kosong
for kode, nilai in kurs.items():
    data.append([kode, f"{nilai:,}".replace(",", ".")])     #menambahkan koma ribuan kemudian ubah koma jadi titik
#menampilkan data, judul kolom dan format tabel
print(tabulate(data, headers=['Kode', 'Kurs'], tablefmt="grid"))

# Input user
matauang_awal = input("dari (IDR/USD/EUR/SGD/JPY): ").upper()   #mengubah input menjadi huruf kapital
matauang_tujuan = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()   #mengubah input menjadi huruf kapital
#menampilkan jumlah dalam desimal
jumlah = float(input("Jumlah: "))
#memanggil fungsi dari konverter
hasil = konversi(matauang_awal, matauang_tujuan, jumlah)

#hasil
print(f"Rp {jumlah:,.0f}".replace(",", "."),
      f"= {hasil:.2f} {matauang_tujuan}")


