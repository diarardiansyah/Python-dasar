# Program angka genap / ganjil

number = int(input('Masukan angka : '))

# membuat kondisi untuk cek angka genap / ganjil
if number % 2 == 0:
    print(f"Angka {number} termasuk ke dalam bilangan genap")
else:
    print(f"Angka {number} termasuk ke dalam bilangan ganjil")