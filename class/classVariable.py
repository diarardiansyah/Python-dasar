class mahasiswa():

    jmlMhs = 0

    def __init__(self, inputNama, inputNim): 
        self.nama = inputNama
        self.nim = inputNim

        mahasiswa.jmlMhs += 1

# Main program

diar = mahasiswa('diar ardiansyah', 2015142104)
ardiansyah = mahasiswa('ardiansyah', 2015142111)

print('Jumlah mahasiswa ada = ',mahasiswa.jmlMhs)