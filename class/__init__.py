# Membuat __init__ python

class mahasiswa():

    def __init__(self, namaInput, nimInput): # init adalah fungsi yang akan dipanggil terlebiih dahulu daripada fungsi yang lain 
        self.name = namaInput
        self.nim = nimInput
    
    def matkul(self):
        print(self.name,'sedang mengikuti mata kuliah kalkulus 2')
    
    def nilai(self, nilaiInput):
        if nilaiInput > 65:
            print(self.name, 'kamu lulus ujian')
        else:
            print(self.name, 'maaf kamu belum lulus ujian')

diar = mahasiswa('Diar ardiansyah', 151544477)

print(diar.name)
print(diar.nim)

diar.matkul()
diar.nilai(60)        