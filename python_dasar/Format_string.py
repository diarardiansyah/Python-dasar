## Belajar format string python

# String
nama = "Diar"
format_str = f"Nama saya adalah = {nama}"
print(format_str)

# Boolean
bool = False
format_str = f"Format boolean adala = {bool}"
print(format_str)

# Number
angka = 10000000
format_str = f"Angka nya adalah = {angka:,}"
print(format_str)

angka = 100.4
format_str = f"Angka nya adalah = {angka}"
print(format_str)

# bilangan desimal
angka = 2111.1211
format_str = f"Angka nya adalah = {angka:.2f}"
print(format_str)

# bilangan leading zero
angka = 1222.9081
format_str = f"Angka nya adalah = {angka:09.1f}"
print(format_str)

# Format angka plus dan minus
number = 20
number1 = -12.121

format_pls = f"Angka plus = {number:+d}"
format_mns = f"Angka minus = {number1:+.1f}"

print(format_pls)
print(format_mns)

# Format angka persen
prsn = 0.1
format_prsn = f"Ängka persen = {prsn:.0%}"
print(format_prsn)

# Format mengitung 
x = 10
y = 10
hitung = f"Hasilnya adalah = {x+y}"
print(hitung)

# Format untuk biner, octal, dan hexadecimal
a = 64
biner = f"Biner nya adalah = {bin(a)}"
octal = f"Octal nya adalah = {oct(a)}"
hexa1 = f"Hexadecimal nya adalah = {hex(a)}"

print(biner)
print(octal)
print(hexa1)
