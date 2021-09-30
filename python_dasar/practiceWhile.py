# Latihan while 1

## varibel untuk angkot nya
jmlAngkot = 10
angkotAktif = 6
noAngkot = 0

# Perulangan untuk perbandingan no angkot dan jumlah angkot
while noAngkot < jmlAngkot:
    noAngkot += 1

    ## Pengcekan angkot nomor berapa saja yang sedang dalam kondisi prima
    if noAngkot <= 6 and noAngkot != 3:
        print(f"angkot no {noAngkot} beroperasi dengan sempurna")
    elif noAngkot == 9 or noAngkot == 3:
        print(f"angkot no {noAngkot} sedang lembur karena kejar setoran")
    else:
        print(f"angkot no {noAngkot} sedang dalam perbaikan")



