# Belajar global variable python

namaOrang = 'Bejo' # variable local
tempatTinggal = 'Jakarta'

# function untk mengubah nama
def ubahNama(namaBaru):
    global namaOrang
    namaOrang = namaBaru
    print(f"nama kamu dirubah menjadi {namaOrang}")

# funtion tempat tinggal
def tempatBaru(nama,newPlace):
    global namaOrang, tempatTinggal
    namaOrang = nama
    tempatTinggal = newPlace
    print(f"Tempat tinggal baru kamu di {tempatTinggal}")

'''
ubahNama('Suneo')
tempatBaru('Ardiansyah','Bekasi')
print(f"nama anda menjadi {namaOrang}, dan saat ini kamu bertempat tinggal di {tempatTinggal}")
'''
# Biodata 
name = 'Diar Ardiansyah'
ttl = '22-12-1996'
umur = '24 Tahun'

def newBiodata(newName,newTtl,newAge):
    global name, ttl, umur # global variable
    name = newName
    ttl = newTtl
    umur = newAge
    print(f"halo saya {name} saya lahir pada tanggal {ttl} dan saat ini saya berusia {umur}")

newBiodata('Ardiansyah', '20-10-1998', '23 Tahun')
print(f"nama saya diubah menjadi {name} dan saya lahir pada tanggal {ttl} dan usia saya {umur}")


