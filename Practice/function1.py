# belajar function python dengan argument

# fungsi dengan menggunakan keywords
def sayuran(nama,warna):
    print(f"nama sayuran {nama} dan warna nya {warna}")

sayuran(nama="brokoli",warna="hijau")

# fungsi dengan argument default
def nama(nama,asal="Jakarta",umur=24):
    print(f"nama saya {nama} saya berasal dari {asal} dan umur saya {umur}")

nama(nama="Diar Ardiansyah")
nama('Diar Ardiansyah',asal='Depok')



