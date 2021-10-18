# Menghitung jumlah kalori yang seharusnya masuk ke dalam tubuh 

print('='*15,'Hitungan BMR untuk laki - laki','='*15)
beratBadan = float(input("Masukan berat badan anda (Kg) : ")) # memasukan inputan user berat badan
tinggiBadan = float(input("Masukan tinggi badan anda (Cm) : ")) # memasukan inputan user tinggi badan
usia = float(input("Masukan usia anda : ")) # memasukan inputan user usia 

result = (88.4 + 13.4  * beratBadan) + (4.8 * tinggiBadan) - (5.68 * usia)
print(f"Maka jumlah kalori yang seharusnya masuk adalah {result:,}")