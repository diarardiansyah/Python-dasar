# Program kalkulator sederhana 

print('======Program kalkulator sederhana python=======')
print('1.Penjumlahan')
print('2.Penguragan')
print('3.Perkalian')
print('4.Pembagian')

# Masukan pilihan operasi perhitungan
inputAngka = float(input('Masukan pilihan operasi perhitungan : '))

angka1 = int(input('Masukan inputan angka anda : '))
angka2 = int(input('Masukan inputan angka anda : '))

# Pengecekan input pilihan dari user
if inputAngka == 1:
    hasil = angka1 + angka2
elif inputAngka == 2:
    hasil = angka1 - angka2
elif inputAngka == 3:
    hasil = angka1 * angka2
elif inputAngka == 4:
    hasil = angka1 / angka2

# Cetak hasil dari perhitungan diatas
print('Hasil dari perhitungan diatas adalah = ', hasil)

# Masukan pilihan operasi perhitungan
inputAngka = float(input('Masukan pilihan operasi perhitungan : '))

angka3 = int(input('Masukan inputan angka anda : '))
angka4 = int(input('Masukan inputan angka anda : '))

# Pengecekan input pilihan dari user
if inputAngka == 1:
    hasil1 = angka3 + angka4
elif inputAngka == 2:
    hasil1 = angka3 - angka4
elif inputAngka == 3:
    hasil1 = angka3 * angka4
elif inputAngka == 4:
    hasil1 = angka3 / angka4

# Cetak hasil dari perhitungan diatas
print('Hasil dari perhitungan diatas adalah = ', hasil1)

# Operator logic boolean
isLogic = (hasil < 5)
print('Maka hasilnya adalah : ', isLogic)

isLogic1 = (hasil1 > 7)
print('Maka hasilnya adalah : ', isLogic1)

hasilAkhir = isLogic or isLogic1
print('Hasil akhir dari OR adalah :', hasilAkhir)

hasilAkhir = isLogic ^ isLogic1
print('Hasil akhir dari XOR adalah :', hasilAkhir)

# lihat type data
print('Type data nya adalah =', type(hasil))




