# Mencari nilai min dan max manual dengan for

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai > nilai_terbesar: # cek apakah nilai > dari nilai terbesar
            nilai_terbesar = nilai # jika ya maka nilai terbesar akan sama dengan nilai
        
    return nilai_terbesar

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]

    for nilai in deret_bilangan:
        if nilai < nilai_terkecil: # cek apakah nilai < dari nilai terkecil
            nilai_terkecil = nilai # jika ya maka nilai terkecil akan sama dengan nilai
        
    return nilai_terkecil

a = [4, 40, 50, -12, 22, 90]
print(a)
print('Nilai terbesar = ', nilai_maksimal(a))
print('Nilai terkecil = ', nilai_minimal(a))
