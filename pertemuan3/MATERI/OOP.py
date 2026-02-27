'''
OOP adalah singkatan dari Object-Oriented Programming (Pemrograman Berorientasi Objek).
Kelas dan objek adalah dua konsep inti dalam pemrograman berorientasi objek.
Sebuah kelas mendefinisikan seperti apa seharusnya sebuah objek, dan sebuah objek dibuat berdasarkan kelas tersebut.
CLASS CETAK BIRU, OBJEK HASIL CETAK BIRU
'''

#MEMBUAT KELAS========================================================================================================================
#MENGGUNAKAN KATA KUNCI CLASS
class MyClass:
  x = 5     #disebut properti

#MEMBUAT OBJEK=========================================================================================================================
# Setiap objek bersifat independen dan memiliki salinan properti kelasnya sendiri.
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)

#HAPUS OBJEK============================================================================================================================
#menghapus objek dengan menggunakan del
del p1

#class Definisi tidak boleh kosong, tetapi jika karena suatu alasan Anda memiliki classdefinisi tanpa konten, tambahkan passpernyataan tersebut untuk menghindari kesalahan.
class Person:
  pass

#Metode_init_Python
#digunakan untuk menetapkan nilai pada properti objek, atau untuk melakukan operasi yang diperlukan saat objek sedang dibuat.
class Person:
  def __init__(self, name, age):
    self.name = name    #properti/atribut
    self.age = age      #properti/atribut
p1 = Person("salwa", 19) 

print(p1.name)  #objek
print(p1.age)

def greet(self):        #method/apa yang bisa dilakukan objeknya
    print("Hello, my name is " + self.name)