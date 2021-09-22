# Belajar string jilid 2

## Menjadikan string menjadi upper and lower case
nama = "diar ardiansyah"
hasil = nama.upper()
print("hasil nya adalah = " + str(hasil))

nama1 = "DiaR ArDianSyah"
hasil = nama1.lower()
print("hasil nya adalah = " + str(hasil))

## Mengecek apakah lower case & upper case true / false
name = "diar"
name_adalah = name.islower()
print(name + " apakah lowercase ? = " + str(name_adalah)) 

name1 = "DIAR"
adalah_name = name1.isupper()
print(name1 + " apakah upper case ? = " + str(adalah_name))

## String method

# isalpha() <-- untuk mengecek semua huruf
coba = ""
hasilnya = coba.isalpha()
print(coba + " hasilnya adalah = " + str(hasilnya))

# isalnum() <-- huruf dan angka
coba1 = "Diar"
hasilnya = coba1.isalnum()
print(coba1 + " hasilnya adalah = " + str(hasilnya))

# isdecimal() <-- angka only
coba3 = "A"
hasilnya = coba3.isdecimal()
print(coba3 + " hasilnya adalah = " + str(hasilnya))

# isspace() <-- cek spasi, tab, dan newline \n
coba4 = " "
hasilnya = coba4.isspace()
print(coba4 + " hasilnya adalah = " + str(hasilnya))

# istitle() <-- semua kata dimulai dengan huruf besar
coba1 = "Si Doel Anak Betawi"
result = coba1.istitle()
print(coba1 + " isTitle = " + str(result))

## mengecek komponen string dengan starswith() & endswith()
judul = "Warkop DKI Reborn".startswith("DKI")
print("startswith = " + str(judul))

judul1 = "Spiderman No Way Home".endswith("Home")
print("endswith = " + str(judul1))

## Mengunakan komponen join() & Split()
test = ['Saya', 'Sangat', 'Ganteng']
hsl = ' '.join(test)
print("hasil join nya adalah = " + str(hsl))

test = ['Saya', 'Sangat', 'Ganteng']
hsl = '='.join(test)
print("hasil join nya adalah = " + str(hsl))

ntest = "Saya=Sangat=Ganteng"
print("hasil splitnya adalah = ", ntest.split("="))

## Alokasi karakter rjust(), ljust(), center()
kanan = "manchester".rjust(15)
print("'"+kanan+"'")

kiri = "manchester".ljust(15)
print("'"+kiri+"'")

center = "manchester".center(16,'#')
print("'"+center+"'")

