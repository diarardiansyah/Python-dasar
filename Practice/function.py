# Belajar function python dasar

# fungsi pertama
def nama1():
    print("Diar Ardiansyah")

# fungsi untuk menghitung harga telur
def telur(kg):
    print("Perhitungan harga telur")
    hargaTelur = 12000
    totalHarga = kg*hargaTelur
    print(f"harga {kg} kg adalah = Rp.{totalHarga:,}")
telur(2)

# fungsi untuk menghitung nilai 
def nilai():
    print(f"Program sederhana nilai mahasiswa")
    inputNama = input("Masukan nama anda : ")
    inputNilai = float(input("Masukan nilai anda : "))
    if inputNilai == 100:
        print(f"selamat {inputNama} kamu lulus ujian dengan nilai sempurna")
    elif inputNilai < 100 and inputNilai >= 85:
        print(f"selamat {inputNama} kamu lulus ujian dengan nilai A")
    elif inputNilai < 85 and inputNilai >= 65:
        print(f"selamat {inputNama} kamu lulus ujian dengan nilai B")
nilai()