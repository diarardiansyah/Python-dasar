print('====== Program ATM dengan python ======\n')

pinRegitered = 789789

inputPin = int(input('Masukan PIN ATM anda : '))

if pinRegitered == inputPin:
    print('==== Pilih opsi berikut ini =====\n')
    print('1. Rp.100.000')
    print('2. Rp.600.000')
    print('3. Rp.1.000.000')
    print('4. Rp.2.000.000')
    print('5. Transfer')

    opsiUser = int(input('Masukan pilihan penarikan anda : '))
    if opsiUser > 5:
        print('Pilihan anda tidak ada di menu')

    elif opsiUser == 5:
        rekTujuan = int(input('Masukan nomor rekening tujuan anda : '))
        jumlahTf = int(input('Masukan jumlah transfer : '))

        if jumlahTf == 0:
            print('Jumlah transfer tidak boleh kosong !!')
        else:
            tanya = input('Jumlah transfer sudah sesuai Ya/Tidak ? ')
            if tanya == 'Ya':
                print('Transaksi sudah selesai dan sudah dikirim ke rekening penerima, Terimakasih')
            else:
                print('Transaksi Gagal!')

    else :
        tanggapanUser = input('Anda yakin untuk melanjutkan transaksi ini Ya/Tidak ? ')
        if tanggapanUser == 'Ya':
            print('Transaksi anda telah selesai')
        else:
            print('Apakah anda mau melanjutkan transaksi yang lainnya ? ')
            
else :
    print('PIN salah')
