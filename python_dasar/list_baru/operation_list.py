# Operasi List 

angka = [1,9,2,1,2,2,29,6,7,0,5,5]

# Menghitung jumlah angka yang ada pada list 
jumlah_angka = angka.count(1)
jmlh_angka = angka.count(2)
print(f"Jumlah angka 1 = {jumlah_angka}\nJumlah angka 2 = {jmlh_angka}")

# Melihat index dari data 
data = ["Harimau","Kuda","Sapi","Ayam","Bebek"]

index_1 = data.index("Bebek")
index_2 = data.index("Sapi")
print(f"Bebek adalah index ke = {index_1}\nSapi adalah index ke = {index_2}")

# Mengurutkan list 
print(f"Data angka sebelum diurutkan = \n{angka}")
angka.sort()
print(f"Data angka sesudah diurutkan = \n{angka}")

# Mengurutkan list dari belakang 
print(f"Data angka pada saat ini = \n{angka}")
angka.reverse()
print(f"Data angka setelah diurutkan dari belakang = \n{angka}")

# Mengurutkan data hewan 
print(f"Data hewan sebelum diurutkan = \n{data}")
data.sort()
print(f"Data hewan setelah diurutkan = \n{data}")

# Melihat angka terbesar dalah list 
angka_terbesar = max(angka)
print(f"Angka terbesar adalah = \n{angka_terbesar}")