class Skincare:
    def __init__(self, faceWash, moist, sunscreen):
        self.faceWash = faceWash    #PROPERTI/ATRIBUT
        self.moist = moist          #PROPERTI/ATRIBUT
        self.sunscreen = sunscreen  #PROPERTI/ATRIBUT

#METHOD
    def pemakaian(self):
        print('dipakai sesuai jenis kulit')

    def kecocokan(self):
        print('jika timbul gatal jangan lanjutkan pemakaian')

#UBAH SALAHSATU PROPERTI
    def ubahskincare(self, cleansingOil):
        self.faceWash = cleansingOil

#OBJEK
paket1 = Skincare('hadalabo', 'hadalabo', 'wardah')
paket2 = Skincare('loreal','loreal','skin1004')
paket3 = Skincare('emina', 'scora', 'you')

#PEMANGGILAN
paket1.kecocokan()
paket1.faceWash = 'lifeboy'
print('sebelum diubah', {paket1.faceWash})



