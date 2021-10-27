# Membuat __init__ python
class mahasiswa():

    def __init__(self, namaInput, nimInput): # init adalah fungsi yang akan dipanggil terlebiih dahulu daripada fungsi yang lain 
        self.name = namaInput
        self.nim = nimInput
    
    def matkul(self):
        print(self.name,'sedang mengikuti mata kuliah kalkulus 2')
    
    def nilai(self, nilaiInput):
       if nilaiInput == 100:
           print(self.name, 'Kamu lulus ujian dengan nilai sempurna')
       
       elif nilaiInput < 100 and nilaiInput >= 80:
           print(self.name, 'Selamat kamu lulus dengan nilai memuaskan')
    
       elif nilaiInput < 80 and nilaiInput >= 65:
           print(self.name, 'Selamat kamu lulus dengan nilai B')
        
       else:
           print(self.name, 'Mohon maaf kamu belum lulus ujian kali ini coba lagi ya')
    

diar = mahasiswa('Diar ardiansyah', 151544477)

print('Nama = ', diar.name)
print('NIM = ', diar.nim)

diar.matkul()
diar.nilai(64)