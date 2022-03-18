# Membuat segitiga dengan bahasa pemrograman python 
sisi = int(input('Masukan sisi = '))

# 1. Menggunakan for 
print('Awal For')

jumlah = 1
for i in range(sisi):
    print('*'*jumlah)
    jumlah += 1

for i in range(sisi):
    print('*'*jumlah)
    jumlah -= 1

print('akhir for')

# 2. Menggunakan while 
print('Awal While')

jumlah = 1
while True:
    print('*'*jumlah)
    jumlah += 1

    if jumlah > sisi:
        break

print('Akhir while')

# 3. Hanya menampilkan jika bilangan ganjil
print('Bilangan ganjil')

jumlah = 1
while True:
    if (jumlah%2):
        # maka akan menampilkan hanya bilangan ganjil
        print('*'*jumlah)
        jumlah += 1
    
    else:
        jumlah += 1
        continue

    if jumlah > sisi:
        break

print('akhir bilangan ganjil')
    