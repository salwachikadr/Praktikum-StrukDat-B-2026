'''
Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.
Tuple adalah salah satu dari 4 tipe data bawaan di Python yang digunakan untuk menyimpan kumpulan data, 3 lainnya adalah List , Set , dan Dictionary , yang semuanya memiliki kualitas dan penggunaan yang berbeda.
Tuple adalah kumpulan yang terurut dan tidak dapat diubah .
Tuple ditulis dengan tanda kurung.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#PANJANG TUPLE
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))       #MENAMPILKAN BERAPA ISI DARI TUPLE

#AKSES TUPLE
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])     #MENAMPILKAN TUPLE INDEKS PERTAMA

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])        #MENGACU PADA INDEKS NEGATIF BERARTI DIMULAI DARI YANG TERAKHIR

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])       #MENAMPILKAN TUPLE YANG DIMUAI DARI 2 SAMPAI 4 SAJA, 5 TIDAK TERMASUK KARENA BATAS AKHIR TIDAK TERMASUK

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:        #PERISKA APAKAH TERDAPAT APPLE DI TUPPLE
  print("Yes, 'apple' is in the fruits tuple")      

  