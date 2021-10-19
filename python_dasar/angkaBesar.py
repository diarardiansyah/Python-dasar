# mengurutkan angka terbesar dari 3 bilangan 

print('===== Mengurutkan angka terbesar =====')

h = int(input("Masukan angka 1 : ")) # input angka pertama
i = int(input("Masukan angka 2 : ")) # input angka kedua
j = int(input("Masukan angka 3 : ")) # input angka ketiga

# membuat kondisi untuk menentukan angka yg terbesar
if h > i and h > j :
    print(f"angka terbesar adalah h : {h}")
elif i > h and i > j:
    print(f"angka terbesar adalah i : {i}")
elif h == i and h == j :
    print(f"angka yang kamu masukan sama bambang!!")
else:
    print(f"angka terbesar adalah j : {j}")