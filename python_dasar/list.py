# Belajar list python dasar

angka = [1,4,5,21,90,100,88,12,10,11]

#akses list 1
number = angka[-4]
print(f"angka nya adalah = {number}")

#slicing list
angka1 = angka[2:5]
angka2 = angka[:5]

#list kedua
angk = [99,121,12,44,54,28,64]

# penggabungan dua list
result = angka + angk
print(f"hasil dari penggabungan list diatas adalah = \n{result}")

#merubah content list
x = angka[:]
x[3] = 22
#print(angka)

# merubah content list dengan metode slicing
angka[4:7] = [69,8,17]
#print(angka)

# list dalam list
y = [angka,angk]
print(y)

# akses list dua dimensi
h = y[0][5]
#print(h)

# menambahkan list dengan method
angka.append(71)
print(angka)

# Menghitung panjang list
panjangList = len(angka)
print(f"Panjang listnya adalah {panjangList}")

# delete data list
delete = angka.pop(10)
print(angka)

panjangList = len(angka)
print(f"Saat ini panjang listnya adalah {panjangList}")