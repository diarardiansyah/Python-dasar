# calculator zakat sederhana

print("=====Aplikasi calculator zakat sederhana=====")

# Ibput nama muzakki
nama = input('Masukan nama anda : ')

# Pertanyaan bekerja atau tidak
tanya = input("Apakah anda saat ini bekerja ? ")

if tanya == "iya":
    penghasilan = float(input("Pengasilan anda perbulan = ")) # menangkap inputan user penghasilan bulanan
    hasil = 0.025 * penghasilan

elif tanya == "tidak" :
    print(f"Anda belum berhak membayar zakat") # Output jika user memasukan inputan belum bekerja 

print("\n============================\n")

# Output program jumlah zakat yang harus dikeluarkan
print(f"Assalamualaikum saudara/saudari {nama} zakat yang harus anda keluarkan Rp. {hasil:,}")