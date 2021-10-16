# membuat biodata dengan list

# list biodata
biodata = [
    'Nama ' '=' ' Diar Ardiansyah',
    'Tempat tanggal lahir ' '=' ' Jakarta, 22 Desember 1996',
    'Usia ' '=' ' 24 Tahun',
    'Pekerjaan ' '=' ' QA engineer'
]

# method append untuk menambah data ke dlam list
biodata.append('Tempat tinggal ' '=' ' Depok')
print(biodata)

# update data di list
biodata[0] = 'Nama ' '=' ' Ardiansyah'
print(f"nama kamu terupdate menjadi {biodata}")

# delete list dengan index
biodata.remove('Tempat tinggal ' '=' ' Depok')
print(f"data list terbaru {biodata}")

