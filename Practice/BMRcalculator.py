print("====== Program menghitung berapa jumlah kalori yang dibutuhkan ======\n")

print("====== Kalkulator BMR untuk laki-laki ======\n")

# masukan nama 
nama = input('Masukan nama anda = ')

# Membuat inputan user berat badan
beratBadan = float(input('Masukan berat badan anda = '))

# Membuat inputan user tinggi badan 
tinggiBadan = float(input('Masukan tinggi badan anda (cm) = '))

# Membuat inputan user usia
usia = float(input('Usia anda saat ini = '))

hitung1 = (88.4 + 13.4 * beratBadan)
hitung2 = (4.8 * tinggiBadan)
hitung3 = (5.68 * usia)

hasil = hitung1 + hitung2 - hitung3

print(f"{nama} Jumlah kalori yang kamu butuhkan perhari adalah = {hasil:,} kalori")