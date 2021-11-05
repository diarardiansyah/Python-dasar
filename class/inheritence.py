class Sayur():

    def __init__(self, namaSayur, warnaSayur, asalSayur):
        self.nama = namaSayur
        self.warna = warnaSayur
        self.asal = asalSayur

    def sayuran(self):
        print('Nama sayur', self.nama, 'Warna sayur', self.warna, 'Dan berasal dari kota', self.asal)

class sayurSayur(Sayur): # <- Class turunan / class inheritence
    pass

    def yursa(self):
        print('Sayur sayurrrrr')

sayur1 = Sayur('Sawi', 'Hijau', 'Semarang')
sayur2 = sayurSayur('Tomat', 'Merah', 'Bandung')

sayur1.sayuran()
sayur2.yursa()