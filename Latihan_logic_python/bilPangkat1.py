print('===== Menghitung bilangan pangkat dengan rekursif =====\n')

bil = int(input('Masukan bilangan : '))
pangkat = int(input('Masukan pangkat : '))

def hitung_pangkat(bil, pangkat):
    if pangkat > 1:
        return bil * hitung_pangkat(bil, pangkat - 1)
    
    return bil

hasil = hitung_pangkat(bil, pangkat)
print(f"hasilnya adalah = {hasil}")
