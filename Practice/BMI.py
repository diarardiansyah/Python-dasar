# Kalulator BMI python

# Kalkulator BMI untuk pria
# Masukan inputan user tinggi badan
print("=====Perhitungan berat badan ideal untuk laki-laki=====")
nama = input("Masukan nama anda = ")
beratBadan1 = float(input("Masukan berat badan anda = "))
tinggiBadan = float(input("Masukan tinggi badan kamu = "))

hasil = tinggiBadan - 100
hasil2 = (tinggiBadan - 100) * float(format(0.1))
result = hasil - hasil2

print(f"Berat badan ideal {nama} adalah = {result}\n")

if beratBadan1 > result:
    print(f"{nama}berat badan kamu tidak ideal")
else:
    print(f"{nama}berat badan kamu ideal")

# Kalulator BMI untuk perempuan
## masukan inputan user tinggi badan
print("=====Perhitungan berat badan ideal untuk perempuan=====")
nama1 = input("Masukan nama anda = ")
beratBadan2 = float(input("Masukan berat badan anda = "))
tinggiBadan1 = float(input("Masukan tinggi badan kamu = "))

x = tinggiBadan1 - 100
y = (tinggiBadan1 - 100) * float(format(0.15))
h = x - y

print(f"berat badan ideal {nama1} adalah {h}")

if beratBadan2 > h:
    print(f"{nama1} berat badan kamu tidak ideal")
else:
    print(f"{nama1} berat badan kamu ideal")



