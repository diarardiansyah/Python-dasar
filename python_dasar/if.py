## Program if python

# Masukan inputan user
nama = "diar ardiansyah"
nilai = float(input("Masukan nilai anda = "))

if nilai==100:
    print("Kamu mendapatkan grade A+ ya " + nama)
elif nilai < 100 and nilai >= 80:
    print("Kamu mendapatkan grade A ya " + nama)
elif nilai < 80 and nilai >= 65:
    print("Kamu mendapatkan grade nilai B ya " + nama)
elif nilai < 65 and nilai >= 50:
    print("Kamu mendapatkan grade nilai C ya " + nama) 
else:
    print("Maaf kamu belum lulus matkul ini")
