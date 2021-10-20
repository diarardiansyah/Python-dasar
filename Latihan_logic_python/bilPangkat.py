# menghitung bilangan pangkat cara standar dengan operator eksponen/pangkat

bil = int(input('Masukan bilangan : '))
pangkat = int(input('Masukan pangkat : '))

# Menggunakan cara dengan operator aritmatika eksponen/pangkat
#hasil = bil ** pangkat
#print(f"Hasilnya adalah = {hasil}")

# Menghitung pangkat cara kedua dengan fungsi pow pada python
hasil = pow(bil, pangkat)
print(f"hasilnya adalah = {hasil}")