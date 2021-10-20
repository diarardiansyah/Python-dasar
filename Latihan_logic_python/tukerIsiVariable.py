# Program pertukaran isi dari variable

makanan1 = 'Mie Ayam'
makanan2 = 'Nasi Goreng'

# untuk menampilkan hasil pertama sebelum data ditukar
print('==== Hasil pertama ====')
print(f"makanan 1 = {makanan1} & makanan 2 = {makanan2} \n")

# membuat variable bantuan utk pertukaran data
makanan3 = makanan1
# proses pertukaran data
makanan1 = makanan2
makanan2 = makanan3

print('==== Hasil kedua ====')
print(f"makanan 1 = {makanan1} & makanan 2 = {makanan2}")