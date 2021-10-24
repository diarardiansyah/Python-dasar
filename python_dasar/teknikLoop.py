# 1. tipe data list 

nama = [ "Nama" " = " "Diar ardiansyah",
         "TTL" " = " "Jakarta 22-12-1996",
         "Usia" " = " "24 Tahun",
         "Pekerjaan" " = " "QA Manual"
]
 
clubBolaFav = [ "Nama Club" " = " "Manchester United",
                "Markas" " = " "Old Trafford",
                "Julukan" " = " "The red devils"
]
 
# Menggunakan fungsi enumerate = memberikan nomor otomatis
for i,x in enumerate(nama):
    print('No',i,':',x)

# Menggunakan fungsi zip
for name,club in zip(nama,clubBolaFav):
    print(f'Biodata diar {name} dan club favoritnya {club}')


# reverse
for i in range(1,5,1):
    print(i)

# tipe data set
binatang = {'kambing','anjing','anoa','zebra','ayam','harimau'}

for x in sorted(binatang):
    print(f'nama nama binatang {x}')