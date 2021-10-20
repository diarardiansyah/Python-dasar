# Mengurutkan angka tengah dari 3 bilangan 

print('===== Mengurutkan angka terkecil =====')

h = int(input('Masukan angka 1 : '))
i = int(input('Masukan angka 2 : '))
j = int(input('Masukan angka 3 : '))

# kondisi untuk mengetahui angka tengah
if(h > i and h < j) or (h < i and h > j):
    print(f"Angka tengah nya adalah H {h}")
elif(i > h and i < j) or (i < h and i > j):
    print(f"Angka tengah nya adalah I {i}")
else:
    print(f"Angka tengah nya adalah J {j}")
