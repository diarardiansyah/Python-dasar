# Aplikasi kasir dengan bahsa pemrograman python 

# 1. Membuat header nama toko dan alamat
print('=== Toko kue Diar Ardiansyah ===\n')
print('=== JL. Jeruk no.90 Rangkepan jaya === \n=== pancoran mas, Depok Jawa Barat ==== \n')

# 2. Membuat inpuran nama kasir
namaKasir = input('Masukan nama anda : ')

# 3. Input harga kue 
hargaKue = int(input('Masukan harga kue : '))

# 4. Input jumlah kue yg di beli
jmlhKue = int(input('Masukan jumlah kue yang di beli : '))

# 5. Hitung total harga kue
totalHarga = hargaKue * jmlhKue

print('\n=================================\n')

print(f"Nama kasir : {namaKasir}")
print(f"Total harga kue yang dibeli adalah Rp. {totalHarga:,}")

print('\n=================================\n')
# 6. Input uang yg diberikan pembeli
uangPembeli = int(input('Uang Pembeli : '))

if uangPembeli == totalHarga:
    print('Uang anda pas tidak ada kembalian')
elif uangPembeli < totalHarga:
    print('Mohon maaf uang anda kurang')
else:
    kembalian = uangPembeli - totalHarga
    print(f"Uang kembalian Rp. {kembalian:,}")

print('Terimakasih telah berbelanja di toko kue kami')


