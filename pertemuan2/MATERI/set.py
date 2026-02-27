'''
Himpunan (set) digunakan untuk menyimpan beberapa item dalam satu variabel.
Set adalah salah satu dari 4 tipe data bawaan di Python yang digunakan untuk menyimpan kumpulan data, 3 lainnya adalah List , Tuple , dan Dictionary , yang semuanya memiliki kualitas dan penggunaan yang berbeda.
Himpunan adalah koleksi yang tidak terurut , tidak dapat diubah* , dan tidak terindeks .
'''
thisset = {"apple", "banana", "cherry"}
print(thisset)

#AKSES SET
#tidak dapat mengakses item dalam suatu himpunan dengan merujuk pada indeks atau kunci.
#Namun Anda dapat melakukan perulangan melalui item-item dalam himpunan menggunakan sebuah for loop, atau menanyakan apakah nilai tertentu ada dalam himpunan, dengan menggunakan inkata kunci.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#PANJANG SET
#MENAMPILKAN PANJANG SET
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#HAPUS SET
#Untuk menghapus item dalam suatu set, gunakan metode remove(), atau discard().
        #1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

        #2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

        #3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()       #Hapus item secara acak dengan menggunakan pop()
print(x)
print(thisset)

