'''
angka1 = float(input("Masukan angka pertama : "))
angka2 = float(input("Masukan angka kedua : "))

def tambah():
    hasil = angka1 + angka2
    print(f"Hasil dari penjumlahan diatas adalah {hasil}")

tambah()
'''
a = 10

for i in range(0, a):
    for x in range(0, i + 1):
        print('* ', end='')
    print('')

b = 10

for o in range(0, b):
    for p in range(0, b - 1):
        print('* ', end='')
    b -= 1    
    print('')
