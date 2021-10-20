# Mengurutkan angka terkecil dari 3 bilangan 

print('===== Mengurutkan angka terkecil =====')

h = int(input('Masukan angka 1 : '))
i = int(input('Masukan angka 2 : '))
j = int(input('Masukan angka 3 : '))

# membuat kondisi untuk menentukan angka terkecil
if h < i and h < j:
    print(f"angka terkecil adalah h {h}")
elif i < h and i < j:
    print(f"angka terkecil adalah i {i}")
elif h == i and h == j:
    print(f"angka yang kamu masukan sama bambank!!")
else:
    print(f"angka terkcecil adalah angka j {j}")