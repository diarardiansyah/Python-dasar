n1 = 0
n2 = 1

n = int(input('Masukan deret angka = '))

for i in range(n):
    if n > 15:
        print('angka yang ente masukin kebanyakan!')
    else:
        print(n1, end=' ')
        hasil = n1 + n2
        n1 = n2 # <- nilai n1 selanjutnya adalah n2 yaitu = 1
        n2 = hasil # <- nilai n2 yaitu 1 sama dengan hasil, yaitu penjumlahan dari n1 + n2