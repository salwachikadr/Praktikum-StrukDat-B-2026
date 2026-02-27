from Kurs import kurs       #Mengambil dict dalam file kurs

def konversi(dari, ke, jumlah):     #membuat fungsi konversi dengan 3 parameter
    if dari == "IDR":               #dari IDR ke mata uang asing (dibagi kurs)
        hasil = jumlah / kurs[ke]   
    else :
        if ke == "IDR":             #Dari mata uang asing ke IDR(dikali kurs)
            hasil = jumlah * kurs[dari]
        else:                       #dari asing ke asing
        # konversi ke IDR dulu
            tentukan_idr = jumlah * kurs[dari]
            #konversi ke mata uang tujuan
            hasil = tentukan_idr / kurs[ke]
    
    return hasil        #mengirim hasil kembali ke main