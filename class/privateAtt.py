# Private attribut python
class siswa():

    kelas = '12 TKJ 5'
    __nilai = 0 # <--Private attribut

    def __init__(self, inputName, inputNis):
        self.nama = inputName
        self.nis = inputNis
    
    def uts(self, inputNilai):
        self.__nilai = inputNilai
    
    def uas(self, inputNilai):
        self.__nilai = inputNilai
    
    def nilaiAkhir(self):
        if self.__nilai <= 50:
            print(self.nama, 'Maaf kamu tidak lulus ujian')
        else:
            print(self.nama, 'Selamat kamu lulus ujian')


diar = siswa('Diar Ardiansyah', 10909012)

diar.uts(20)
diar.uas(70)
diar.nilaiAkhir()

print(diar.kelas)
print(diar.__nilai)



    