# Komparasi and logic

# Program sederhana untuk komparasi and logic
print('======Latihan Komparasi dan logic========')
isNumber = float(input('Masukan angka kurang dari 4 dan lebih dari 10 : '))

# Cek angka yang lebih dari 4
isBelow = (isNumber < 4)
print('Maka hasilnya adalah :', isBelow)

# cek angka yang kurang dari 10
isAbove = (isNumber > 10)
print('Maka hasilnya adalah :', isAbove)

# masukan operator logika
isHasil = isBelow or isAbove
print('Maka hasilnya adalah :', isHasil)


print('=======Latihan Komparasi dan Logic')
isNumber = float(input('Masukan angka yang lebih dari 4 dan kurang dari 11 : '))

# cek angka yang lebih dari 4
isAbove = (isNumber > 4)
print('Maka hasilnya adalah : ',isAbove)

# cek angka yang kurang dari 11
isBelow = (isNumber < 11)
print('Maka hasilnya adalah : ',isBelow)

# Masukan operator logika
isHasil = isAbove and isBelow
print('Hasil akhirnya adalah : ', isHasil)