# calculator zakat sederhana

print("=====Aplikasi calculator zakat sederhana=====")

# fungsi untuk perhitungan zakat
def zakat():
    # Pertanyaan bekerja atau tidak
    tanya = input("Apakah anda saat ini bekerja ? ")
    if tanya == "iya":
        penghasilan = float(input("Pengasilan anda perbulan = ")) # menangkap inputan user penghasilan bulanan
    elif tanya == "tidak" :
        penghasilan = float(input("Pengasilan anda perbulan = ")) # menangkap inputan user penghasilan bulanan
    hasil = 0.025 * penghasilan
    if hasil == 0:
        print(f"anda belum berhak untuk menunaikan zakat")
    else :
        print(f"zakat yang harus anda keluarkan adalah Rp.{hasil:,}")
    return hasil
    
zakat()

# tanpa menggunakan function
'''
penghasilan = float(input("Penghasilan anda perbulan = "))
hasil = 0.025 * penghasilan
print(f"Zakat yang harus anda keluarkan Rp.{hasil:,}")
'''
