
class sayur():

    __jmlSayur = 0

    def __init__(self, InputNama, inputJenis):
        self.nama = InputNama
        self.jenis = inputJenis
    
    def banyakSayur(self, inputBanyak):
        self.__jmlSayur += inputBanyak
    
    def banyakSayur1(self, inputBanyak):
        self.__jmlSayur += inputBanyak

    def akhir(self):
        if self.__jmlSayur < 10:
            print('Jumlah sayur', self.nama, 'tidak mencukupi')
        else:
            print('Jumlah sayur', self.nama, 'mencukupi')

# Main Program

brokoli = sayur('Brokoli', 'Hijau')
kangkung = sayur('Kangkung', 'Hijau')


print(brokoli.nama)

brokoli.banyakSayur(1)
brokoli.banyakSayur1(10)
brokoli.akhir()

kangkung.banyakSayur(1)
kangkung.banyakSayur1(5)
kangkung.akhir()

