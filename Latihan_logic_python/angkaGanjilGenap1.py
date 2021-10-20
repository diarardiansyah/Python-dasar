# Program untuk menampilkan angka ganjil dan genap berdasarkan range angka

# memasukan inputan user
range1 = int(input('Masukan angka pertama : '))
range2 = int(input('Masukan angka kedua : '))

print("Masukan Pilihan \n 1.Ganjil \n 2.Genap")

userChoose = int(input('Masukan pilihan anda : '))

# membuat kondisi jika pilihan yang dimasukan bukan angka 1 dan 2
if userChoose not in [1, 2]:
    print('Pilihan yang anda masukan tidak tersedia di program ini! ')
else:
    for x in range(range1, range2 + 1): # membuat looping untuk menampilkan angka sesuai range
        if userChoose == 1 and x % 2 == 1: # kondisi 1 untuk output bilangan ganjil
            print(x, end = ' ')
        elif userChoose == 2 and x % 2 == 0: # kondisi 2 untuk output bilangan genap
            print(x, end = ' ')
        else:
            print('')

