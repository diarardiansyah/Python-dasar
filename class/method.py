# Belajar class python
class namaGuru():
    name = 'nama'

    def mapel(self,tambahan): # Note = self adlaah argument yang sudah menempel di dalam object, object disini yaitu suryadi & sinta
        print('====Belajar method python====')
        print(self.name,'Mengajar mata pelajaran penjaskes',tambahan)
    
    def mapel1(self,tambahan1):
        print('====Belajar method python====')
        print(self.name,'Mengajar mata pelajaran IPA',tambahan1)
    
# Main program
suryadi = namaGuru()
sinta = namaGuru()

suryadi.name = 'suryadi yadi'
sinta.name = 'sinta tata'

print(suryadi.name)
print(sinta.name)

suryadi.mapel('dan cara mengajar nya sangat asik')
sinta.mapel1('dan jadi guru paling cantik yang ada di sekolah ini')