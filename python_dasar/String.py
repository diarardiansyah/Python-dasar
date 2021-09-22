# Belajar string

#print("Diar ardinsyah, \nArdiansyah")

#print(r"""
#Nama : Diar 
#Jabatan : QA manual 
#Tempat Lahir : Jakarta//asas\n
#""")

# Belajar string Python 

# 1. Menggabungkan nama depan nama tengah dan nama belakang
nama_depan = "diar"
nama_tengah = "A"
nama_akhir = "Ardiansyah"

fullName = nama_depan + " " + nama_tengah + " " + nama_akhir
print("Nama lengkap saya adalah " + fullName)

# 2. Menghitung panjang string
panjangStr = len(fullName)
print("Panjang string dari " + fullName + " adalah = " + str(panjangStr))

# 3. Opeator string
d = "H"
status = d in fullName
print("karakter " + d + " ada di fullName = " + str(status))

d1 = "y"
status = d1 in fullName
print("karakter " + d1 + " ada di fullName = " + str(status))

d2 = "a"
status = d2 not in fullName
print("karakter " + d2 + " tidak ada di fullName = " + str(status))

# 4.Cetak string berkali kali
print(10*"wk")

# 5.Indexing string
print("index ke [0] = " + fullName[0])
print("index ke [1] = " + fullName[2])
print("index ke [-1] = " + fullName[-1])

# Mengambil index string berdasarkan range
print("index ke [0-8] = " + fullName[0:9]) # note = apabila ingin mengambil range string index nya harus + 1
print("index ke [9-12] = " + fullName[9:13])

# Mengambil index string longkap 3
print("index ke [3,6,9,12] = " + fullName[3:13:3])

# Mengambil string terkecil 
print("String terkecil adalah = ", min(fullName))

# Mengambil string terbesar
print("String terbesar adalah = ", max(fullName))

# Ascii code string
ascii_code = ord("y")
print("ASCII code nya adalah = " + str(ascii_code))

x = 117
print("String nya adalah = " + chr(x))

# Operator menghitung jumlah cahracter 
name = "diar ardiansyah sangat ganteng"
jmlh = name.count("a")
print("Jumlah character a nya adalah = " + str(jmlh))